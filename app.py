from flask import *
from werkzeug.security import generate_password_hash, check_password_hash
from config import db
import time
import config

app = Flask(__name__)

# 从对象中导入config
app.config.from_object(config)



@app.route('/')
def index():
    return render_template('index.html')


# 注册页面
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        email = request.form.get('email')
        nickname = request.form.get('nickname')
        password_1 = request.form.get('password_1')
        password_2 = request.form.get('password_2')
        phone = request.form.get('phone')
        if not all([email,nickname,password_1,password_2,phone]):
            flash("信息填写不全，请将信息填写完整")
            return render_template('register.html')
        if password_1 != password_2:
            flash("两次密码填写不一致！")
            return render_template('register.html')
        password = generate_password_hash(password_1, method="pbkdf2:sha256", salt_length=8)
        try:
            cur = db.cursor()
            sql = "select * from UserInformation where email = '%s'"%email
            db.ping(reconnect=True)
            cur.execute(sql)
            result = cur.fetchone()
            if result is not None:
                flash("该Email已存在！")
                return render_template('register.html')
            else:
                create_time = time.strftime("%Y-%m-%d %H:%M:%S")
                sql = "insert into UserInformation(email, nickname, password, type, create_time, phone) VALUES ('%s','%s','%s','0','%s','%s')" %(email,nickname,password,create_time,phone)
                db.ping(reconnect=True)
                cur.execute(sql)
                db.commit()
                cur.close()
                return redirect(url_for('index'))
        except Exception as e:
            raise e

if __name__ == '__main__':
    app.run()
