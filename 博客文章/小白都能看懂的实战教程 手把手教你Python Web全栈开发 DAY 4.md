> 大家好，我叫亓官劼（qí guān jié ）,这个《小白都能看懂的实战教程 手把手教你Python Web全栈开发》是一个零基础的实战教程，手把手带你开发一套系统，带你了解Python web全栈开发，目前正在连续更新中，如果喜欢的话可以点赞关注博主，后面会持续更新。

[博客文章内容导航（实时更新）](https://blog.csdn.net/qq_43422111/article/details/105174460)
**更多优质文章推荐：**
 - [小白都能看懂的实战教程 手把手教你Python Web全栈开发 (DAY 1)](https://blog.csdn.net/qq_43422111/article/details/105141834)
 - [小白都能看懂的实战教程 手把手教你Python Web全栈开发 (DAY 2)](https://blog.csdn.net/qq_43422111/article/details/105148494)
 - [小白都能看懂的实战教程 手把手教你Python Web全栈开发 (DAY 3)](https://blog.csdn.net/qq_43422111/article/details/105160371)
 - [小白都能看懂的实战教程 手把手教你Python Web全栈开发 (DAY 4)](https://blog.csdn.net/qq_43422111/article/details/105160371)
- [Flask学习,(基本语法)](https://blog.csdn.net/qq_43422111/article/details/104304290)
- [一文教会你Bootstrap，让你也可以快速建站](https://blog.csdn.net/qq_43422111/article/details/105098288)
- [一文教你如何白嫖JetBrains全家桶（IDEA/PtChram/CLion）免费正版](https://blog.csdn.net/qq_43422111/article/details/105128206)
- [一本教你如何在前端实现富文本编辑器](https://blog.csdn.net/qq_43422111/article/details/105160915)

本项目所有源码在GitHub开源，GitHub地址为：[OnlineForumPlatform](https://github.com/qiguanjie/OnlineForumPlatform)有需要源码可以前去查看，喜欢的话可以star一下

## 小白都能看懂的实战教程 手把手教你Python Web全栈开发  第四讲
&emsp;&emsp;在前面的三讲中，我们完成了项目的创建，导航条、注册、登录、论坛页面、发布帖子等功能的实现，目前我们的系统已经可以发布和查看我们的帖子了，并且可以登录我们的账号。下面我们就来继续完善我们的系统，让他看查看每个帖子的详情，并且能够回复帖子等功能。

### 4.1 帖子详情页面、帖子回复实现
&emsp;&emsp;帖子详情页面的数据库我们已经在第三讲中实现了，就是我们的Issue和Comment表，下面我们来一起实现以下帖子详情页面的前端和后端功能，让它能够展示各个帖子的一个详情页面。

#### 4.1.1 帖子详情页面实现-后端
&emsp;&emsp;这里我们先实现帖子详情页面的后端，因为我们发现如果先做前端的话，在做后端的话，还需要对前端进行一定的修改，这样不利于我们这样文章式的进行表述。所以我们在这里先做后端的功能，这里先创建一个issue_detail.html页面，留作后面的前端使用。
&emsp;&emsp;如果要进入我们的帖子详情页面，那么首先我们需要一个参数，就是我们Ino(Issue的编号)，因为这个编号是唯一表示我们的帖子的。所以在这里我们写帖子详情的路由的时候就和前面不太一样了，我们需要使用一个带参数的路由，用来接收这个Ino,跳转到我们相对应的帖子详情。
```python
# 问题详情
@app.route('/issue/<Ino>')
def issue_detail(Ino):
    return render_template('issue_detail.html')
```
在有了Ino之后，我们就可以根据Ino来对数据库中的文章数据进行查找了。下面我们来思考我们需要返回到前端的数据由哪些呢？我们主要需要下面这项数据:
- 文章标题
- 每章每层楼的内容，包括：
  - 评论内容
  - 作者昵称
  - 评论发布时间
  - 楼号（Cno）

我们主要就是需要这几项数据，数据里面的文章标题的每个问题详情页面固定的一个标题，每层楼的内容的每层楼不一样的，所以两个我们分别进行查询。
```python
# 问题详情
@app.route('/issue/<Ino>')
def issue_detail(Ino):
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
            return render_template('issue_detail.html',Ino=Ino,issue_title=issue_title,comment=comment)
    except Exception as e:
        raise e
```
这就是目前简单的后端逻辑，虽说我们目前只有get请求方式，这里也限定一下，为了安全起见。

#### 4.1.2 帖子详情页面实现-前端
&emsp;&emsp;前端的话，我们这里为了便于理解，前端还是精简布局（博主直男审美，写不出漂亮的UI）即可。我们需要一个页头来显示我们的标题，然后下面使用一个`<ul></ul>`显示我们的帖子详情即可，在`<li></li>`中固定一个div，每层楼的结构固定，然后再在中间填充上我们从后端获取到的数据即可。前端的文件这里我们使用issue_detail.html和issue_detail.css。详细的结构可以去看我的GitHub,每一次博客更新之后我都会把源代码push到GitHub中。
&emsp;&emsp;这里直接上代码吧，前端的代码和前面基本一样，前面已经各个步骤都仔细讲解过了，如果前端部分的还有不清楚的可以看看前面的。
issue_detail.html:
```html
{% extends 'base.html' %}

{% block title %}
    {{ issue_title }}
{% endblock %}

{% block css %}
<link rel="stylesheet" href="/static/css/issue_detail.css">
{% endblock %}

{% block content %}
<div class="formula_content">
    <div class="page-header" id="page_header">
        <h1>{{ issue_title }}</h1>
    </div>
    <div class="issue_list_div">
        <ul class="issue_list_ul">
            {% for comm in comment %}
                <li class="issue_list_li">
                    <div class="issue_div">
                        <div class="issue_content">
                            <article>
                                {{ comm[1]|safe }}
                            </article>
                        </div>
                        <div class="author_info">
{#                            <p class="cno_info">{{ comm[3] }}</p>#}
                            <p class="info">
                                <span class="cno_info">{{ comm[3] }}楼</span>&emsp;
                                <span>
                                    <span>作者：{{ comm[0] }}</span>&emsp;&emsp;
                                    <span>发布时间：{{ comm[2] }}</span>
                                </span>
                            </p>
                        </div>
                    </div>
                </li>
            {% endfor %}
        </ul>
    </div>
</div>
{% endblock %}
```
issue_detail.css：
```css
.formula_content{
    margin: 5% 20%;
}

#page_header{
    text-align: center;
}

.issue_list_ul{
    list-style-type: none;
    margin-left: 0;
    padding-left: 0;
}
.author_info{
    text-align: right;
}

.issue_div{
    border-bottom:1px solid #eee;
}

.issue_content{
    min-height: 88px;
}

.post-info{
    text-align: right;
}

.cno_info{
    text-align: left;
}

```

&emsp;&emsp;有仔细的小伙伴是不是发现了，这里前端的部分和论坛页面的前端基本类似，只不过改掉了其中显示的内容而已。页面效果为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200330190007339.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)

#### 4.1.3 帖子回复实现-前端
&emsp;&emsp;这里其实有点纠结放在哪里的，直接放在帖子详情的下面也可以，单独一个页面也可以，原本是打算单独一个页面的，因为那样的话，会比较放富文本编辑器和Markdown编辑器的双编辑器。不过又想了想，使用Markdown回复帖子的人应该不多，所以这里就放在下面的吧，使用富文本编辑器。如果想做双编辑器的话也可以自己稍作修改。
&emsp;&emsp;这里只需要在最后添加一个`<li></li>`然后再嵌套一个div，然后添加一个富文本编辑器的实例即可，还不会在前端实现富文本编辑器的可以去看看博主之前的文章：[一本教你如何在前端实现富文本编辑器](https://blog.csdn.net/qq_43422111/article/details/105160915)
这里就直接上修改完的代码和效果图吧：
issue_detail.html:
```html
{% extends 'base.html' %}

{% block title %}
    {{ issue_title }}
{% endblock %}

{% block css %}
    <link rel="stylesheet" href="/static/css/issue_detail.css">
    <!-- 引入配置文件 -->
    <script src="/static/ueditor/ueditor.config.js"}></script>
    <!-- 引入编辑器源码文件 -->
    <script src="/static/ueditor/ueditor.all.min.js"}></script>
{% endblock %}

{% block content %}
<div class="formula_content">
    <div class="page-header" id="page_header">
        <h1>{{ issue_title }}</h1>
    </div>
    <div class="issue_list_div">
        <ul class="issue_list_ul">
            {% for comm in comment %}
                <li class="issue_list_li">
                    <div class="issue_div">
                        <div class="issue_content">
                            <article>
                                {{ comm[1]|safe }}
                            </article>
                        </div>
                        <div class="author_info">
{#                            <p class="cno_info">{{ comm[3] }}</p>#}
                            <p class="info">
                                <span class="cno_info">{{ comm[3] }}楼</span>&emsp;
                                <span>
                                    <span>作者：{{ comm[0] }}</span>&emsp;&emsp;
                                    <span>发布时间：{{ comm[2] }}</span>
                                </span>
                            </p>
                        </div>
                    </div>
                </li>
            {% endfor %}
                <li>
                    <div>
                        <form class="post_issue_form" method="post">
                            <input type="hidden" name="Ino" value="{{ Ino }}">
                            <div class="ueditor_div">
                                <script id="editor" type="text/plain">
                                请输入回复的内容!
                                </script>
                            </div>
                            <div id="post_issue_butt">
                              <button type="submit" class="btn btn-default">回复</button>
                            </div>
                        </form>
                    </div>
                </li>
        </ul>
    </div>
<!-- 实例化编辑器 -->
<script type="text/javascript">
    var editor = UE.getEditor('editor');
</script>
</div>
{% endblock %}
```
效果图：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200330191338696.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
下面我们就要来实现后端的功能了。

#### 4.1.3 帖子回复实现-后端
后端的话，我们需要做的就是将回复人的email、回复时间、回复楼号、回复内容存储进数据库中，并显示。这里由于我们是在同一个页面中进行回复，所以我们要使用到POST方法进行传输数据。下面我们首先将这些需要存储的数据在服务器端获取到：
```python
Ino = request.values.get('Ino')
email = session.get('email')
comment = request.form.get('editorValue')
comment_time = time.strftime("%Y-%m-%d %H:%M:%S")
```
这里的Cno需要来查找数据库中的最大Cno,然后进行+1所得。问题详情完整代码为：帖子回复实现的代码主要为POST请求部分：
```python
# 问题详情
@app.route('/issue/<Ino>', methods=['GET', 'POST'])
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
```
页面效果：![在这里插入图片描述](https://img-blog.csdnimg.cn/20200330194548796.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
**这里提醒一下各位，在测试回复和发布帖子的时候一定要登录账号，这里还没有完善过滤器功能，下面进行完善** 

### 4.2访问过滤功能实现
&emsp;&emsp;在上面发布帖子和回复帖子的时候是不是有很多小伙伴都都发现在未登录的时候进行发布会报错？是因为我们的email是函数依赖于UerInformation表的，如果未登录的话则没有，也就无法插入到数据库中。同时还有很多功能页面我们是针对不同用户的，比如有的管理员功能页面，我们就不能让普通用户和访客进入，有些页面我们只想让登陆的用户进行查看，那我们就要让访客无法访问。
&emsp;&emsp;下面我们就来实现这个功能，要使用这个功能，我们就需要使用Python的装饰器功能。如果对装饰器这个功能不太了解也没关系，我们这边只需要一些简单的功能即可。我会在代码中进行详细的进行注释。我们将装饰器放在decorators.py文件中。我们这里先简单的写一个限制登录的装饰器，如下。
```python
from functools import wraps
from flask import session, url_for, redirect


# 登录限制的装饰器 用于某些只让登录用户查看的网页
def login_limit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 我们这里用来区分是否登录的方法很简答，就是查看session中是否赋值了email，如果赋值了，说明已经登录了
        if session.get('email'):
            # 如果登录了，我们就正常的访问函数的功能
            return func(*args, **kwargs)
        else:
            # 如果没登录，我们就将它重定向到登录页面，这里大家也可以写一个权限错误的提示页面进行跳转
            return redirect(url_for('login'))

    return wrapper
```
&emsp;&emsp;写完之后，我们在app.py中导入它`from decorators import login_limit` 然后再每一个我们需要进行登录限制的路由之后加上我们的装饰器`@login_limit`即可，此时我们需要进行限制登录的两个页面就是我们的发布帖子页面和我们的帖子详情页面需要进行一个限制。进行限制之后，如果我们没登录的时候进行发布帖子就会自动的跳转到登录页面，提醒你进行登录啦~
这里在贴一下到目前为止app.py的完整文件代码吧：
```python
from flask import *
from werkzeug.security import generate_password_hash, check_password_hash
from config import db
import random
import time
import config
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
            sql = "select Issue.Ino, Issue.email,UserInformation.nickname,issue_time,Issue.title,Comment.comment from Issue,UserInformation,Comment where Issue.email = UserInformation.email and Issue.Ino = Comment.Ino order by issue_time DESC "
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


if __name__ == '__main__':
    app.run()
```

今天的第四讲就先到这里， 这一讲的内容大家都成功运行起来了吗？大家都学会这些功能了吗？如果还没学会，可以再往前看看呦，我们下一讲再见~
