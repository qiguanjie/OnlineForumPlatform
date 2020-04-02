from flask import *
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from config import db
import random
import time
import config
import os
import re
from decorators import login_limit

app = Flask(__name__)

# 从对象中导入config
app.config.from_object(config)


# 登录状态保持
@app.context_processor
def login_status():
    # 从session中获取email
    email = session.get('email')
    # 如果有email信息，则证明已经登录了，我们从数据库中获取登陆者的昵称和用户类型，来返回到全局
    if email:
        try:
            cur = db.cursor()
            sql = "select nickname,type from UserInformation where email = '%s'" % email
            db.ping(reconnect=True)
            cur.execute(sql)
            result = cur.fetchone()
            if result:
                return {'email': email, 'nickname': result[0], 'user_type': result[1]}
        except Exception as e:
            raise e
    # 如果email信息不存在，则未登录，返回空
    return {}


# 主页
@app.route('/')
def index():
    return render_template('index.html')


# 注册页面
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        email = request.form.get('email')
        nickname = request.form.get('nickname')
        password_1 = request.form.get('password_1')
        password_2 = request.form.get('password_2')
        phone = request.form.get('phone')
        if not all([email, nickname, password_1, password_2, phone]):
            flash("信息填写不全，请将信息填写完整")
            return render_template('register.html')
        if password_1 != password_2:
            flash("两次密码填写不一致！")
            return render_template('register.html')
        password = generate_password_hash(password_1, method="pbkdf2:sha256", salt_length=8)
        try:
            cur = db.cursor()
            sql = "select * from UserInformation where email = '%s'" % email
            db.ping(reconnect=True)
            cur.execute(sql)
            result = cur.fetchone()
            if result is not None:
                flash("该Email已存在！")
                return render_template('register.html')
            else:
                create_time = time.strftime("%Y-%m-%d %H:%M:%S")
                sql = "insert into UserInformation(email, nickname, password, type, create_time, phone) VALUES ('%s','%s','%s','0','%s','%s')" % (
                    email, nickname, password, create_time, phone)
                db.ping(reconnect=True)
                cur.execute(sql)
                db.commit()
                cur.close()
                return redirect(url_for('index'))
        except Exception as e:
            raise e


# 登录页面
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if not all([email, password]):
            flash("请将信息填写完整！")
            return render_template('login.html')
        try:
            cur = db.cursor()
            sql = "select password from UserInformation where email = '%s'" % email
            db.ping(reconnect=True)
            cur.execute(sql)
            result = cur.fetchone()
            if result is None:
                flash("该用户不存在")
                return render_template('login.html')
            if check_password_hash(result[0], password):
                session['email'] = email
                session.permanent = True
                cur.close()
                return redirect(url_for('index'))
            else:
                flash("密码错误！")
                return render_template('login.html')
        except Exception as e:
            raise e


# 用户注销
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for(('index')))


# 生成128随机id
def gengenerateID():
    re = ""
    for i in range(128):
        re += chr(random.randint(65, 90))
    return re


# 发布帖子
@app.route('/post_issue', methods=['GET', 'POST'])
@login_limit
def post_issue():
    if request.method == 'GET':
        return render_template('post_issue.html')
    if request.method == 'POST':
        title = request.form.get('title')
        comment = request.form.get('editorValue')
        email = session.get('email')
        issue_time = time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            cur = db.cursor()
            Ino = gengenerateID()
            sql = "select * from Issue where Ino = '%s'" % Ino
            db.ping(reconnect=True)
            cur.execute(sql)
            result = cur.fetchone()
            # 如果result不为空，即存在该ID，就一直生成128位随机ID,直到不重复位置
            while result is not None:
                Ino = gengenerateID()
                sql = "select * from Issue where Ino = '%s'" % Ino
                db.ping(reconnect=True)
                cur.execute(sql)
                result = cur.fetchone()
            sql = "insert into Issue(Ino, email, title, issue_time) VALUES ('%s','%s','%s','%s')" % (
                Ino, email, title, issue_time)
            db.ping(reconnect=True)
            cur.execute(sql)
            db.commit()
            sql = "insert into Comment(Cno, Ino, comment, comment_time, email) VALUES ('%s','%s','%s','%s','%s')" % (
                '1', Ino, comment, issue_time, email)
            db.ping(reconnect=True)
            cur.execute(sql)
            db.commit()
            cur.close()
            return redirect(url_for('formula'))
        except Exception as e:
            raise e


# 论坛页面
@app.route('/formula')
def formula():
    if request.method == 'GET':
        try:
            cur = db.cursor()
            sql = "select Issue.Ino, Issue.email,UserInformation.nickname,issue_time,Issue.title,Comment.comment from Issue,UserInformation,Comment where Issue.email = UserInformation.email and Issue.Ino = Comment.Ino and Cno = '1' order by issue_time DESC "
            db.ping(reconnect=True)
            cur.execute(sql)
            issue_information = cur.fetchall()
            cur.close()
            return render_template('formula.html', issue_information=issue_information)
        except Exception as e:
            raise e


# 问题详情
@app.route('/issue/<Ino>', methods=['GET', 'POST'])
@login_limit
def issue_detail(Ino):
    if request.method == 'GET':
        try:
            if request.method == 'GET':
                cur = db.cursor()
                sql = "select Issue.title from Issue where Ino = '%s'" % Ino
                db.ping(reconnect=True)
                cur.execute(sql)
                # 这里返回的是一个列表，即使只有一个数据，所以这里使用cur.fetchone()[0]
                issue_title = cur.fetchone()[0]
                sql = "select UserInformation.nickname,Comment.comment,Comment.comment_time,Comment.Cno from Comment,UserInformation where Comment.email = UserInformation.email and Ino = '%s'" % Ino
                db.ping(reconnect=True)
                cur.execute(sql)
                comment = cur.fetchall()
                cur.close()
                # 返回视图，同时传递参数
                return render_template('issue_detail.html', Ino=Ino, issue_title=issue_title, comment=comment)
        except Exception as e:
            raise e

    if request.method == 'POST':
        Ino = request.values.get('Ino')
        email = session.get('email')
        comment = request.values.get('editorValue')
        comment_time = time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            cur = db.cursor()
            sql = "select max(Cno) from Comment where Ino = '%s' " % Ino
            db.ping(reconnect=True)
            cur.execute(sql)
            result = cur.fetchone()
            Cno = int(result[0]) + 1
            Cno = str(Cno)
            sql = "insert into Comment(Cno, Ino, comment, comment_time, email) VALUES ('%s','%s','%s','%s','%s')" % (
            Cno, Ino, comment, comment_time, email)
            cur.execute(sql)
            db.commit()
            cur.close()
            return redirect(url_for('issue_detail',Ino = Ino))
        except Exception as e:
            raise e


# 个人中心
@app.route('/personal')
@login_limit
def personal():
    if request.method == 'GET':
        email = session.get('email')
        try:
            cur = db.cursor()
            sql = "select email, nickname, type, create_time, phone from UserInformation where email = '%s'" % email
            db.ping(reconnect=True)
            cur.execute(sql)
            personal_info = cur.fetchone()
        except Exception as e:
            raise e
        return render_template('personal.html',personal_info = personal_info)


# 修改密码
@app.route('/change_password',methods=['GET','POST'])
@login_limit
def change_password():
    if request.method == 'GET':
        return render_template('change_password.html')
    if request.method == 'POST':
        old_password = request.form.get('old_password')
        new_password1 = request.form.get('new_password1')
        new_password2 = request.form.get('new_password2')
        if not all([old_password,new_password1,new_password2]):
            flash("信息填写不全！")
            return render_template('change_password.html')
        if new_password1 != new_password2:
            flash("两次新密码不一致！")
            return render_template('change_password.html')
        email = session.get('email')
        try:
            cur = db.cursor()
            sql = "select password from UserInformation where email = '%s'" % email
            db.ping(reconnect=True)
            cur.execute(sql)
            password = cur.fetchone()[0]
            if check_password_hash(password,old_password):
                password = generate_password_hash(new_password1, method="pbkdf2:sha256", salt_length=8)
                sql = "update UserInformation set password = '%s' where email = '%s'" % (password,email)
                db.ping(reconnect=True)
                cur.execute(sql)
                db.commit()
                cur.close()
                return render_template('index.html')
            else:
                flash("旧密码错误！")
                return render_template('change_password.html')
        except Exception as e:
            raise e

# 查看已发布的帖子
@app.route('/show_issue')
@login_limit
def show_issue():
    if request.method == 'GET':
        email = session.get('email')
        try:
            cur = db.cursor()
            sql = "select ino, email, title, issue_time from Issue where email = '%s' order by issue_time desc" % email
            db.ping(reconnect=True)
            cur.execute(sql)
            issue_detail = cur.fetchall()
        except Exception as e:
            raise e
        return render_template('show_issue.html',issue_detail=issue_detail)

# 生成120位随机id
def gengenerateFno():
    re = ""
    for i in range(120):
        re += chr(random.randint(65, 90))
    return re

# 资源上传页面
@app.route('/post_file',methods=['GET','POST'])
@login_limit
def post_file():
    if request.method == 'GET':
        return render_template('post_file.html')
    if request.method == 'POST':
        email = session.get('email')
        upload_file = request.files.get('file')
        filename = request.form.get('filename')
        file_info = request.form.get('file_info')
        file_path = 'store'
        file_time = time.strftime("%Y-%m-%d %H:%M:%S")
        Fno = gengenerateFno()
        try:
            cur = db.cursor()
            sql = "select * from Files where Fno = '%s'" % Fno
            db.ping(reconnect=True)
            cur.execute(sql)
            result = cur.fetchone()
            # 如果result不为空，即该Fno已存在时，一直生成随机的Fno，只到该数据库中不存在
            while result is not None:
                Fno = gengenerateFno()
                sql = "select * from Files where Fno = '%s'" % Fno
                db.ping(reconnect=True)
                cur.execute(sql)
                result = cur.fetchone()
            # 获取文件的后缀
            upload_name = str(upload_file.filename)
            houzhui = upload_name.split('.')[-1]
            # 保存在本地的名字为生成的Fno+文件后缀，同时修改Fno的值
            Fno = Fno+"."+houzhui
            # 保存文件到我们的服务器中
            upload_file.save(os.path.join(file_path,Fno))
            # 将文件信息存储到数据库中
            sql = "insert into Files(Fno, filename, file_info, file_time,email) VALUES ('%s','%s','%s','%s','%s')" % (Fno,filename,file_info,file_time,email)
            db.ping(reconnect=True)
            cur.execute(sql)
            db.commit()
            cur.close()
            return redirect(url_for('source'))
        except Exception as e:
            raise e

# 资源专区
@app.route('/source')
def source():
    if request.method == 'GET':
        try:
            cur = db.cursor()
            sql = "select Fno,filename,file_info,file_time,nickname from Files,UserInformation where Files.email = UserInformation.email"
            db.ping(reconnect=True)
            cur.execute(sql)
            files = cur.fetchall()
            cur.close()
            return render_template('source.html',files = files)
        except Exception as e:
            raise e

# 在线查看文件
@app.route('/online_file/<Fno>')
def online_file(Fno):
    return send_from_directory(os.path.join('store'), Fno)

# 文件下载功能
@app.route('/download/<Fno>')
def download(Fno):
    return send_file(os.path.join('store') + "/" + Fno, as_attachment=True)

if __name__ == '__main__':
    app.run()
