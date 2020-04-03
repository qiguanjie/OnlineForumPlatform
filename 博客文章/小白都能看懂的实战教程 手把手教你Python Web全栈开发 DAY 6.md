> 大家好，我叫亓官劼（qí guān jié ）,这个《小白都能看懂的实战教程 手把手教你Python Web全栈开发》是一个零基础的实战教程，手把手带你开发一套系统，带你了解Python web全栈开发，目前正在连续更新中，如果喜欢的话可以点赞关注博主，后面会持续更新。

 [博主博客文章内容导航（实时更新）](https://blog.csdn.net/qq_43422111/article/details/105174460)
**更多优质文章推荐：**
 - [小白都能看懂的实战教程 手把手教你Python Web全栈开发 (DAY 1)](https://blog.csdn.net/qq_43422111/article/details/105141834)
 - [小白都能看懂的实战教程 手把手教你Python Web全栈开发 (DAY 2)](https://blog.csdn.net/qq_43422111/article/details/105148494)
 - [小白都能看懂的实战教程 手把手教你Python Web全栈开发 (DAY 3)](https://blog.csdn.net/qq_43422111/article/details/105160371)
 - [小白都能看懂的实战教程 手把手教你Python Web全栈开发 (DAY 4)](https://blog.csdn.net/qq_43422111/article/details/105202794)
- [小白都能看懂的实战教程 手把手教你Python Web全栈开发 (DAY 5)](https://blog.csdn.net/qq_43422111/article/details/105230847)
- [一本教你如何在前端实现富文本编辑器](https://blog.csdn.net/qq_43422111/article/details/105160915)
- [小白都能看得懂的教程 一本教你如何在前端实现markdown编辑器](https://blog.csdn.net/qq_43422111/article/details/105238029)
- [Flask学习(基本语法)](https://blog.csdn.net/qq_43422111/article/details/104304290)
- [一文教会你Bootstrap，让你也可以快速建站](https://blog.csdn.net/qq_43422111/article/details/105098288)
- [一文教你如何白嫖JetBrains全家桶（IDEA/PtChram/CLion）免费正版](https://blog.csdn.net/qq_43422111/article/details/105128206)

## 小白都能看懂的实战教程 手把手教你Python Web全栈开发 (DAY 6)
&emsp;&emsp;今天来到我们实战系列的第六天，在之前的五天里，我们已经完成了在线论坛系统的导航条、登录、注册、论坛页面、帖子详情页面、个人页面、修改密码、查看已发布帖子等的功能实现，目前我们的论坛已经可以进行帖子发布，查看帖子详情，并且进行回复信息了。在上一讲中，我们还是实现了功能限制，对不同用户的访问进行过滤。下面我们继续来完善我们的这个在线论坛系统，今天我们来为这个系统添加资源专区，这里我们主要分为资源上传，资源列表（查看资源列表），在线查看资源文件、资源文件下载的功能。

### 6.1资源上传功能实现
&emsp;&emsp;这里我们来开始实现资源上传功能，我们先从前端开始实现，然后到后端进行存储。之前写过一篇如何实现文件上传下载的博文，如果对这方面还不太了解的同学，可以先去看一下博文：[Python Flask文件上传下载](https://blog.csdn.net/qq_43422111/article/details/104301593)，这篇博文简单的介绍了如何实现文件的上传与下载，这里我们来进行一个详细的实现。
#### 6.1资源上传功能实现-前端
&emsp;&emsp;资源文件上传，我们这里设计一个`<div>`，然后里面放一个`<form>`，进行文件的上传，和文件描述。这里先创建一个post_file.html文件用来当前的前端的文件，post_file.css文件用来记录样式。我们这个页面还是继承自`base.html`。还是先上个效果图，然后我们给一个源码，因为这里前端的话，我们就是一个`<table>`然后里面放3行的信息。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200402205728798.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
这里我们需要注意的就是，在我们的form中，不要忘记设置`enctype`,需要把这个属性设置为`multipart/form-data`。
post_file.html:
```html
{% extends 'base.html' %}

{% block title %}
资源上传
{% endblock %}

{% block css %}
<link rel="stylesheet" href="/static/css/post_file.css">
{% endblock %}

{% block content %}
<div class="post_file_content">
    <div class="page-header" id="page_header">
      <h1>资源上传<small>Resource upload</small></h1>
    </div>
    <div class="post_file_div">
        <form action="" method="post" enctype="multipart/form-data">
            <table id="file_table">
                <tr>
                    <td>
                        选择你需要上传的文件
                    </td>
                    <td>
                        <input id="file_butt" type="file" name="file">
                    </td>
                </tr>
                <tr>
                    <td>
                        请输入文件名称：
                    </td>
                    <td>
                        <div class="form-group">
                            <input type="text" class="form-control" name="filename" id="exampleInputEmail1" placeholder="请输入文件名称：">
                        </div>
                    </td>
                </tr>
                <tr>
                    <td>
                        请输入文件描述信息：
                    </td>
                    <td>
                        <div class="form-group">
                            <input type="text" class="form-control" name="file_info" id="exampleInputEmail1" placeholder="请输入文件描述信息：">
                        </div>
                    </td>
                </tr>
                <tr>
                    <td colspan="2">
                        <div id="login_butt">
                          <button type="submit" class="btn btn-default">上传</button>
                      </div>
                    </td>
                </tr>
            </table>
        </form>
    </div>
</div>
{% endblock %}
```
post_file.css
```css
.post_file_content{
    margin-top: 8%;;
    margin-left: 25%;
    margin-right: 25%;
}

#page_header{
    text-align: center;
}

#file_table td{
    width: 200px;
}
#login_butt{
    text-align: center;
}
```

#### 6.1.2资源上传功能实现-数据库端
&emsp;&emsp;这里我们又需要新增一个表了，用来存储我们的一个文件的存储信息，我们主要存储的信息有：Fno（用来唯一标识我们的文件）、文件名称、文件描述信息、文件上传时间。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200402223327976.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
SQL语句为：
```sql
create table Files
(
	Fno varchar(128) not null,
	filename nvarchar(128) default '未命名' null,
	file_info nvarchar(128) default '没有描述信息' null,
	file_time datetime null,
	email varchar(128) null,
	constraint Files_UserInformation_email_fk
		foreign key (email) references UserInformation (email)
);

create unique index Files_Fno_uindex
	on Files (Fno);

alter table Files
	add constraint Files_pk
		primary key (Fno);


```

#### 6.1.3资源上传实现-后端
&emsp;&emsp;下面我们来实现我们资源上传的数据库端，首先我们需要在我们的项目文件中创建一个文件夹用来存放我们上传的文件。这里创建了一个store文件夹用于存放上传的文件。![在这里插入图片描述](https://img-blog.csdnimg.cn/20200402204645710.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
下面我们就来讲从前端发送的文件保存到我们的服务器的文件夹中。这里为了服务器文件的安全性，我们这里文件的名称采用再次命名，一来可以防止重复的文件名，二来可以防止文件名称中有一些特殊的字符。我们这里的文件名称采用随机的120字符，然后加上原本文件的后缀组成，这里可以防止本地存储位置的文件有重复。在代码中有各个步骤的详细注解，大家可以查看代码中的信息：
```python
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
            return render_template('index.html')
        except Exception as e:
            raise e
```

&emsp;&emsp;这样我们就可以将我们的文件上传到我们是服务器端，并且保存到我们制定的文件夹中了。

### 6.2 资源专区功能实现
&emsp;&emsp;下面我们开始来实现我们的资源专区，这里的资源专区我们用来显示我们的所有的资源的一个列表，并且可以进行在线查看资源和下载资源。

#### 6.2.1 资源专区功能实现-后端
&emsp;&emsp;资源专区的话，我们还是先实现后端，发送数据到前端，然后我们前端将接收到的数据进行一个排版，然后显示。大家有没有发现一个问题，我们刚刚先实现了资源的上传，但是我们并没有导航，那为什么我们要先实现资源上传呢？因为如果我们先实现资源专区的话，没有东西显示，用于测试啊~所以我们先实现资源上传，可以先上传文件，便于资源专区的实现。
&emsp;&emsp;这里我们需要返回到前端的数据有Fno、文件名、文件描述、创建时间和创建人的昵称。
```python
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
```

#### 6.2.2资源专区功能实现-前端
&emsp;&emsp;资源专区的前端我们首先需要一个列表用来展示我们的服务器中已上传的文件的信息，并且导航到我们的文件在线查看，文件下载等功能。这里使用source.html用来实现我们的前端功能，使用source.css存放样式的描述信息。页面效果为：![在这里插入图片描述](https://img-blog.csdnimg.cn/20200402225119633.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
在这里由于我们的在线查看文件和下载文件还没有实现，所有我们这里的超链接的地址是#，等下我们来进行实现。目前的前端的页面代码为：
```html
{% extends 'base.html' %}

{% block title %}
资源专区
{% endblock %}

{% block css %}
<link rel="stylesheet" href="/static/css/source.css">
{% endblock %}

{% block content %}
<div class="source_content">
    <div class="page-header" id="page_header">
      <h1>资源专区<small>Resources Zone</small></h1>
    </div>
    <div class="source_div">
        <ul class="source_ul">
            {% for file in files %}
                <li class="issue_list_li">
                    <div class="issue_div">
                        <div class="issue_content">
                            <h3>
                                <a href="#">
                                    {{ file[1] }}
                                </a>
                            </h3>
                            <article>
                                {{ file[2] }}
                            </article>
                        </div>
                        <div class="author_info">
                            <p class="post-info">
                                <span>上传者：{{ file[4] }}</span>&emsp;&emsp;
                                <span>上传时间：{{ file[3] }}</span>&emsp;
                                <span><a href="#">在线查看</a></span>&emsp;
                                <span><a href="#">下载文件</a></span>
                            </p>
                        </div>
                    </div>
                </li>
            {% endfor %}
        </ul>
    </div>
</div>
{% endblock %}
{% block source_class %}
active
{% endblock %}
```
source.css:
```css
.source_content{
    margin-right: 20%;
    margin-left: 20%;
    margin-top: 8%;
}

.author_info{
    text-align: right;
}

.source_ul{
    list-style-type: none;
    margin-left: 0;
    padding-left: 0;
}
#page_header{
    text-align: center;
}
```
&emsp;&emsp;我们在base.html中添加了资源专区的导航，并且添加了source_class的block，如果不修改base.html的话，需要将source.html的最后3行删除，不然会报错。base中插入的代码为`                <li class="{% block source_class %}{% endblock %}"><a href="{{ url_for('source') }}">资源专区</a></li>
`插入在论坛导航的下面一行。

#### 6.2.3 实现文件在线查看功能
&emsp;&emsp;其实这里面要想实现文件的在线查看功能非常的容易实现，我们只需要返回这个文件即可。我们这里需要在路由处传递一个参数Fno，用来寻找我们的文件。
```python
# 在线查看文件
@app.route('/online_file/<Fno>')
def online_file(Fno):
    return send_from_directory(os.path.join('store'), Fno)
```

#### 6.2.4 实现文件下载功能
&emsp;&emsp;我们再来实现我们的文件下载功能，这个也是非常简单的，我们直接返回一个send_file即可实现文件的下载。
```python
# 文件下载功能
@app.route('/download/<Fno')
def download(Fno):
    return send_file(os.path.join('store') + "/" + Fno, as_attachment=True)
```

在实现完我们的文件在线查看和文件下载之后，我们就可以修改我们的资源专区的前端，为其超链接添加一个正确的链接，让他能够实现正确的功能了。修改后的souce.html页面为：
```html
{% extends 'base.html' %}

{% block title %}
资源专区
{% endblock %}

{% block css %}
<link rel="stylesheet" href="/static/css/source.css">
{% endblock %}

{% block content %}
<div class="source_content">
    <div class="page-header" id="page_header">
      <h1>资源专区<small>Resources Zone</small></h1>
    </div>
    <div class="source_div">
        <ul class="source_ul">
            {% for file in files %}
                <li class="issue_list_li">
                    <div class="issue_div">
                        <div class="issue_content">
                            <h3>
                                <a href="{{ url_for('online_file',Fno = file[0]) }}">
                                    {{ file[1] }}
                                </a>
                            </h3>
                            <article>
                                {{ file[2] }}
                            </article>
                        </div>
                        <div class="author_info">
                            <p class="post-info">
                                <span>上传者：{{ file[4] }}</span>&emsp;&emsp;
                                <span>上传时间：{{ file[3] }}</span>&emsp;
                                <span><a href="{{ url_for('online_file',Fno = file[0]) }}">在线查看</a></span>&emsp;
                                <span><a href="{{ url_for('download',Fno = file[0]) }}">下载文件</a></span>
                            </p>
                        </div>
                    </div>
                </li>
            {% endfor %}
        </ul>
    </div>
</div>
{% endblock %}
{% block source_class %}
active
{% endblock %}
```
&emsp;&emps;然后我们这里再为我们上传资源的页面添加一个导航，由于我们上传资源的功能只有登录的用户才可以进行使用，所以我们在导航栏中添加，当我们登录时，显示上传资源的导航，我们在base.html中添加:（加在资源专区后面即可）
```html
{% if email %}
	<li class="{% block post_file_class %}{% endblock %}"><a href="{{ url_for('post_file') }}">上传资源</a></li>
{% endif %}
```
为了防止我们有的小伙伴不知道插入到哪里，我们这里再贴一下目前base.html整体的代码
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>
        {% block title %}
{#        其他页面重写标题的地方#}
        {% endblock %}
    </title>
    {% block css %}
{#    其他页面引用样式或者js的地方#}
    {% endblock %}
    <link rel="stylesheet" href="/static/css/base.css">
    <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
    <script src="https://cdn.bootcss.com/twitter-bootstrap/3.4.0/js/bootstrap.min.js"></script>
    <link href="https://cdn.bootcss.com/twitter-bootstrap/3.4.0/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="navigation_bar">
        <nav class="navbar navbar-default">
          <div class="container-fluid">
{#              由于这里我们不需要使用商标，所以对Bran部分进行了删除#}
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
              <ul class="nav navbar-nav">
                <li class="{% block index_class %}{% endblock %}"><a href="{{ url_for('index') }}">首页<span class="sr-only">(current)</span></a></li>
                <li class="{% block formula_class %}{% endblock %}"><a href="{{ url_for('formula') }}">论坛</a></li>
                <li class="{% block source_class %}{% endblock %}"><a href="{{ url_for('source') }}">资源专区</a></li>
                {% if email %}
                    <li class="{% block post_file_class %}{% endblock %}"><a href="{{ url_for('post_file') }}">上传资源</a></li>
                {% endif %}
              </ul>
              <form class="navbar-form navbar-left">
                <div class="form-group">
                  <input type="text" class="form-control" placeholder="Search">
                </div>
                <button type="submit" class="btn btn-default">Submit</button>
              </form>
              <ul class="nav navbar-nav navbar-right">
                {% if email %}
                    <li class="{% block post_issue_class %}{% endblock %}"><a href="{{ url_for('post_issue') }}">发布帖子</a></li>
                    <li class=""><a href="{{ url_for('register') }}">注销</a></li>
                    <li class="dropdown">
                      <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{{ nickname }} <span class="caret"></span></a>
                      <ul class="dropdown-menu">
                        <li><a href="{{ url_for('personal') }}">个人中心</a></li>
                        <li><a href="{{ url_for('change_password') }}">修改密码</a></li>
                        <li role="separator" class="divider"></li>
                        <li><a href="{{ url_for('show_issue') }}">已发布的帖子</a></li>
                      </ul>
                    </li>
                {% else %}
                    <li class="{% block register_class %}{% endblock %}"><a href="{{ url_for('register') }}">注册</a></li>
                    <li class="{% block login_class %} {% endblock %}"><a href="{{ url_for('login') }}">登录</a></li>
                {% endif %}
              </ul>
            </div><!-- /.navbar-collapse -->
          </div><!-- /.container-fluid -->
        </nav>
    </div>
    <div class="content" style="padding: 0;margin: 0;">
        {% block content %}
{#        其他页面重写页面内容的地方#}
        {% endblock %}
    </div>
</body>
</html>
```

&emsp;&emsp;然后我们app.py中的返回值也可以进行一个适当的优化，例如我们上传完资源之后可以重定向到我们的资源专区，而不是一开始的index(因为当时还没有资源专区)。所以这里也贴一下我们app.py的全部代码，给小伙伴们进行一个参考
```python
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
```

&emsp;&emsp;目前我们的项目35583行代码了，这里面其实有很多代码是我们引入的插件的代码和我们富文本编辑器的代码，我们把它去掉，我们纯手动码的代码也有3982行代码了，也算一个五脏俱全的小项目了，这期我们暂时就先到这里了，我们后续再慢慢的更新我们的一个持续优化，其实分栏里有剩下改进的种种方法，例如Markdown编辑器：[小白都能看得懂的教程 一本教你如何在前端实现markdown编辑器](https://blog.csdn.net/qq_43422111/article/details/105238029)等，大家可以前去查看。
&emsp;&emsp;如果喜欢本系列，欢迎关注博客，查看更多文章！