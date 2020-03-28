## 小白都能看懂的实战教程 手把手教你Python Web全栈开发 Flask(Python Web)实战系列之在线论坛系统    第二讲
这是小白都能看懂的实战教程 手把手教你Python Web全栈开发 的第二讲，如果文中有基础知识不太熟悉的话，可以看博主前几期的博客：
小白都能看懂的实战教程 手把手教你Python Web全栈开发 Flask(Python Web)实战系列之在线论坛系统    第一讲：[小白都能看懂的实战教程 手把手教你Python Web全栈开发 第一讲](https://blog.csdn.net/qq_43422111/article/details/105141834)
Flask基本语法：[Flask学习（一）博客地址](https://blog.csdn.net/qq_43422111/article/details/104304290)
Bootstrap用法：[一文教会你Bootstrap，让你也可以快速建站](https://blog.csdn.net/qq_43422111/article/details/105098288)
白嫖开发环境（IDEA/Pycharm/Clion）：[一文教你如何白嫖JetBrains全家桶（IDEA/PtChram/CLion）免费正版](https://blog.csdn.net/qq_43422111/article/details/105128206)
本项目所有源码在GitHub开源，GitHub地址为：[OnlineForumPlatform](https://github.com/qiguanjie/OnlineForumPlatform)
有需要源码可以前去查看，喜欢的话可以star一下
在做完准备工作之后，我们就正式的开始开发了，在这本系列的第二讲中，博主将带领你实现在线论坛系统的导航条、注册、登录和主页功能，在实现的同时会讲解各个功能实现的原理，手把手的教你进入Python Web全栈开发，一个字一个字的代码完成本项目。

@[TOC](本文目录)
### 2.1 导航栏实现
我们首先从导航栏开始开发，每个页面需要有导航栏，可以说一个非常常用的组件了。这里我们先创建一个hmtl页面base.html进行开发导航栏相关功能，将文件建立在templates文件夹中。
在这里先说明一下为什么要使用base.html这个名字，因为Jinja2模板是支持继承机制的，而导航栏又是几乎每个页面都需要使用到的一个组件，所以我们这里将导航栏这个文件base.html作为一个基类，其他所有的视图文件都继承自它，并在它的基础上进行重写相关的内容，实现各个视图的不同内容。
在创建完文件之后，由于我们这个项目前端UI部分使用Bootstrap进行快速建站，还有不会Bootstarp的同学可以看一下之前的这篇教程：[什么？你还不会Bootstrap？一文教会你Bootstrap，让你也可以快速建站](https://blog.csdn.net/qq_43422111/article/details/105098288)

我们这里选择一个3.4.0的版本，在html中引入：
```html
<script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>
<script src="https://cdn.bootcss.com/twitter-bootstrap/3.4.0/js/bootstrap.min.js"></script>
<link href="https://cdn.bootcss.com/twitter-bootstrap/3.4.0/css/bootstrap.min.css" rel="stylesheet">
```

在引用完成之后，我们先去bootstrap样式库中找一个喜欢的导航条样式，然后加入到我们的base.html中。
我们这里使用这个样式的，直接加入到base.html中：
```html
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#">Brand</a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
        <li><a href="#">Link</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="#">Action</a></li>
            <li><a href="#">Another action</a></li>
            <li><a href="#">Something else here</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">Separated link</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">One more separated link</a></li>
          </ul>
        </li>
      </ul>
      <form class="navbar-form navbar-left">
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Search">
        </div>
        <button type="submit" class="btn btn-default">Submit</button>
      </form>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#">Link</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="#">Action</a></li>
            <li><a href="#">Another action</a></li>
            <li><a href="#">Something else here</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">Separated link</a></li>
          </ul>
        </li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
```
插入之后我们打开网页就可以看到如下效果：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200325162947164.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)

然后我们在根据我们的需求，对这个导航条进行一定的更改，并且为base.html页面划分几个block。
暂时先修改为这样，后续我们加完导航之后，还需再对各个标定的页面进行一个修改。修改之后的完整代码为：
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
                <li class="active"><a href="#">首页<span class="sr-only">(current)</span></a></li>
                <li><a href="#">Link</a></li>
                <li class="dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
                  <ul class="dropdown-menu">
                    <li><a href="#">Action</a></li>
                    <li><a href="#">Another action</a></li>
                    <li><a href="#">Something else here</a></li>
                    <li role="separator" class="divider"></li>
                    <li><a href="#">Separated link</a></li>
                    <li role="separator" class="divider"></li>
                    <li><a href="#">One more separated link</a></li>
                  </ul>
                </li>
              </ul>
              <form class="navbar-form navbar-left">
                <div class="form-group">
                  <input type="text" class="form-control" placeholder="Search">
                </div>
                <button type="submit" class="btn btn-default">Submit</button>
              </form>
              <ul class="nav navbar-nav navbar-right">
                <li><a href="#">Link</a></li>
                <li class="dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
                  <ul class="dropdown-menu">
                    <li><a href="#">Action</a></li>
                    <li><a href="#">Another action</a></li>
                    <li><a href="#">Something else here</a></li>
                    <li role="separator" class="divider"></li>
                    <li><a href="#">Separated link</a></li>
                  </ul>
                </li>
              </ul>
            </div><!-- /.navbar-collapse -->
          </div><!-- /.container-fluid -->
        </nav>
    </div>
    <div>
        {% block content %}
{#        其他页面重写页面内容的地方#}
        {% endblock %}
    </div>
</body>
</html>
```
这里暂时加了3个block，分别是title：标题。css:引用css样式和js脚本。content：页面主题内容部分。
导航栏的剩下内容将会在项目开发的过程中逐渐完善，因为它涉及多个页面，下面我们进行下一项功能页面。

### 2.2 注册功能实现
#### 2.2.1  注册功能实现-数据库
在实现注册功能的时候，我们首先就需要在数据库中创建一个表来存储我们的注册信息了。这个项目预设2端（普通用户端和管理员端），那么我们表中需要存储用户的信息有：用户名（这里使用邮箱），昵称，密码，用户的权限，注册时间，联系方式等信息，我们这里暂定收集用户名，昵称，密码，用户的权限，注册时间，联系方式，这6种信息用于注册，下面我们创建一个UserInformation表。这里可以使用pychram右面的Database使用图像界面创建，也可以使用命令行创建。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200327193002692.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)SQL语句为：
```SQL
create table UserInformation
(
	email varchar(128) not null,
	nickname nvarchar(100) default '未设置昵称' null,
	password varchar(128) not null,
	type int default '0' null,
	create_time datetime default '1999-9-9 9:9:9' not null,
	phone varchar(128) null,
	constraint UserInformation_pk
		primary key (email)
);

```
这样我们一个用于存储用户信息的表就创建好了，下面我们来设计一个注册的前端页面。

#### 2.2.2  注册功能实现-前端
在写前端页面之前，由于我们每个页面都是继承自base.html，因此我们可以写个extend.html来方便我们每次进行继承，在此基础上进行开发。
extend.html页面代码为：
```html
{% extends 'base.html' %}

{% block title %}

{% endblock %}

{% block css %}

{% endblock %}

{% block content %}

{% endblock %}
```

下面我们就正式的开始写register.html页面了。
首先我们去bootstrap样式库中去找个页头，为页面添加一个大标题。
```html
<div class="page-header">
  <h1>Example page header <small>Subtext for header</small></h1>
</div>
```

为了方便我们实时的调试我们的页面，我们先在app.py中为注册页面添加一个路由：
```python
from flask import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('base.html')


# 注册页面
@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run()

```
这样我们访问http://127.0.0.1:5000/register就可以实时查看我们页面的信息了，方便我们对UI部分进行调试，设计一个自己喜欢的UI。在引入页头之后，我们访问发现页面有点差强人意，左对齐一点也不好看，我们可以让他居中。我们在static/css文件夹中创建一个register.css来为register.html提供样式。创建完之后我们在register.html中引入这个css。
```html
<link rel="stylesheet" href="/static/css/register.css">
```
下面我们就来选择一个表单进行设计一个注册页面。这里调整UI部分比较简单并且繁琐，所以就不一步一步的记录了，在调整完之后贴上完整的代码，给大家看一下整体的效果。

初步设计之后，register.css:
```css
#page_header{
    text-align: center;
}

.register_content{
    /*调整边距，调到相对中间的位置*/
    margin:10% 25%;
}

#register_butt{
    text-align: center;
}
```
register.html:
```html
{% extends 'base.html' %}

{% block title %}
注册
{% endblock %}

{% block css %}
<link rel="stylesheet" href="/static/css/register.css">
{% endblock %}

{% block content %}
<div class="register_content">
    <div class="page-header" id="page_header">
      <h1>注册<small>Register</small></h1>
    </div>
    <div id="register_form">
        <form method="post">
          <div class="form-group">
            <label for="exampleInputEmail1">Email address</label>
            <input type="email" class="form-control" name="email" id="exampleInputEmail1" placeholder="Email address">
          </div>
          <div class="form-group">
            <label for="exampleInputEmail1">昵称</label>
            <input type="text" class="form-control" name="nickname" id="exampleInputEmail1" placeholder="昵称">
          </div>
          <div class="form-group">
            <label for="exampleInputPassword1">密码</label>
            <input type="password" class="form-control" name="password_1" id="exampleInputPassword1" placeholder="密码">
          </div>
            <div class="form-group">
            <label for="exampleInputPassword1">确认密码</label>
            <input type="password" class="form-control" name="password_2" id="exampleInputPassword1" placeholder="确认密码">
          </div>
          <div class="form-group">
            <label for="exampleInputEmail1">联系方式</label>
            <input type="text" class="form-control" name="phone" id="exampleInputEmail1" placeholder="联系方式">
          </div>
          <div id="register_butt">
              <button type="submit" class="btn btn-default">注册</button>
              <button type="button" class="btn btn-default" onclick="location.href='#'">登录</button>
          </div>
        </form>
    </div>

</div>
{% endblock %}
```

页面效果为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200327211428459.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
整体还是简洁大方的，下面我们在针对注册页面修改一下导航条，在导航条中添加到注册页面的导航，并且添加一个block来标定上面选取的页面。
修改之后的base.html为：
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
                <li class="{% block homepage_class %}{% endblock %}"><a href="#">首页<span class="sr-only">(current)</span></a></li>
                <li><a href="#">Link</a></li>
                <li class="dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
                  <ul class="dropdown-menu">
                    <li><a href="#">Action</a></li>
                    <li><a href="#">Another action</a></li>
                    <li><a href="#">Something else here</a></li>
                    <li role="separator" class="divider"></li>
                    <li><a href="#">Separated link</a></li>
                    <li role="separator" class="divider"></li>
                    <li><a href="#">One more separated link</a></li>
                  </ul>
                </li>
              </ul>
              <form class="navbar-form navbar-left">
                <div class="form-group">
                  <input type="text" class="form-control" placeholder="Search">
                </div>
                <button type="submit" class="btn btn-default">Submit</button>
              </form>
              <ul class="nav navbar-nav navbar-right">
                <li class="{% block register_class %}{% endblock %}"><a href="{{ url_for('register') }}">注册</a></li>
                <li><a href="#">登录</a></li>
{#                <li class="dropdown">#}
{#                  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>#}
{#                  <ul class="dropdown-menu">#}
{#                    <li><a href="#">Action</a></li>#}
{#                    <li><a href="#">Another action</a></li>#}
{#                    <li><a href="#">Something else here</a></li>#}
{#                    <li role="separator" class="divider"></li>#}
{#                    <li><a href="#">Separated link</a></li>#}
{#                  </ul>#}
{#                </li>#}
              </ul>
            </div><!-- /.navbar-collapse -->
          </div><!-- /.container-fluid -->
        </nav>
    </div>
    <div>
        {% block content %}
{#        其他页面重写页面内容的地方#}
        {% endblock %}
    </div>
</body>
</html>

```

同时在对register.html中进行添加block register_class，添加完成之后的register.html为：
```html
{% extends 'base.html' %}

{% block title %}
注册
{% endblock %}

{% block css %}
<link rel="stylesheet" href="/static/css/register.css">
{% endblock %}

{% block content %}
<div class="register_content">
    <div class="page-header" id="page_header">
      <h1>注册<small>Register</small></h1>
    </div>
    <div id="register_form">
        <form method="post">
          <div class="form-group">
            <label for="exampleInputEmail1">Email address</label>
            <input type="email" class="form-control" name="email" id="exampleInputEmail1" placeholder="Email address">
          </div>
          <div class="form-group">
            <label for="exampleInputEmail1">昵称</label>
            <input type="text" class="form-control" name="nickname" id="exampleInputEmail1" placeholder="昵称">
          </div>
          <div class="form-group">
            <label for="exampleInputPassword1">密码</label>
            <input type="password" class="form-control" name="password_1" id="exampleInputPassword1" placeholder="密码">
          </div>
            <div class="form-group">
            <label for="exampleInputPassword1">确认密码</label>
            <input type="password" class="form-control" name="password_2" id="exampleInputPassword1" placeholder="确认密码">
          </div>
          <div class="form-group">
            <label for="exampleInputEmail1">联系方式</label>
            <input type="text" class="form-control" name="phone" id="exampleInputEmail1" placeholder="联系方式">
          </div>
          <div id="register_butt">
              <button type="submit" class="btn btn-default">注册</button>
              <button type="button" class="btn btn-default" onclick="location.href='#'">登录</button>
          </div>
        </form>
    </div>

</div>
{% endblock %}

{% block register_class %}
active
{% endblock %}

```

调整之后的注册页面为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200327212443543.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
当在注册页面时，会将注册的导航着重显示。同时在导航条上添加了注册和登录页面的导航。


#### 2.2.3  注册功能实现-后端
下面我们就来实现注册的服务器端功能，将前端发送的信息检查，如果不正确则返回提示，如果正确则将用户信息存储到数据库中。
既然要使用到数据库，那我们就先来配置一下config.py，这个文件主要存放项目的配置信息。
这里我们设置一下SECRET_KEY和db。
config.py:
```python
# encoding:utf-8
import os
import pymysql

DEBUG = False

SECRET_KEY = os.urandom(24)

db = pymysql.connect(host='localhost', user='root', password='password1q!', db='OnlineForumPlatform', port=3306)

```
配置完成之后我们在app.py中导入config.py，并且绑定配置。
```python
from flask import *
import config

app = Flask(__name__)

# 从对象中导入config
app.config.from_object(config)
```

然后我们开始写注册的后端逻辑功能。本系列第一次写后端代码，这里做一个详细的说明，有Flask基础不错的同学可以直接跳到后面的整体代码。
由于我们路由默认的请求方式只有一种是GET请求，但是我们注册的话，为了安全，form表单一般使用POST请求，因此我们这里先设置请求方式：
```python
@app.route('/register',methods=['GET','POST'])
```

然后我们再获取前端表单的信息：
```python
email = request.form.get('email')
nickname = request.form.get('nickname')
password_1 = request.form.get('password_1')
password_2 = request.form.get('password_2')
phone = request.form.get('phone')
```
在获取完之后我们就需要对这些数据进行处理了，首先我们要检查数据是否完整，如果信息填写不完整肯定是不可以注册的，我们返回提示，这里我们使用flash传递提示回到注册页面。
```python
        if not all([email,nickname,password_1,password_2,phone]):
            flash("信息填写不全，请将信息填写完整")
            return render_template('register.html')
```
既然使用flash进行传递消息，那我们就需要在前端将flash消息显示出来。我们将这段代码放到前端合适的一个位置，这个位置自己选择一个显眼的位置即可。这里我讲这个信息提示放在了页头的下方。
```html
<span style=" font-size:20px;color: red" >
	{% for item in get_flashed_messages() %}
		{{ item }}
	{% endfor %}
</span>
```
下面继续来完善我们的后端，信息填写完整之后，我们还需要验证两次密码输入的是否一致，如果不一致，则需要返回错误提示。
```python
if password_1 != password_2:
	flash("两次密码填写不一致！")
	return render_template('register.html')
 ```

如果信息都填写正确了，那下面我们开始对密码进行加密，我们这里使用的是pbkdf2:sha256加密方式，对密码进行128位的散列加密，可以极大的保护用户信息的安全性。要使用这个加密，我们需要导入它：
```python
from werkzeug.security import generate_password_hash, check_password_hash
```
然后我们使用generate_password_hash来加密我们的密码，由于password_1和password_2是一样的，那么我们只需要加密password_1即可：
```python
password = generate_password_hash(password_1, method="pbkdf2:sha256", salt_length=8)
```
这样我们的准备工作就完成了，下面我们开始将信息存储到数据库中：
首先我们要将我们config文件中配置的db导入进来：
```python
from config import db
```
然后我们来获取db的cursor，来进行相关数据库操作，这里我们使用Python直接操纵数据库，当然，大家也可以使用Flask-SQLAlchemy来进行操作数据库，这里就使用Python直接操纵数据库的方式进行。
首先我们要检查我们的数据库中email是否存在，即当前用户是否已经存在，我们使用email进行唯一表示用户，所以不允许重复，我们还需要检查一下email。
```python
try:
	cur = db.cursor()
	sql = "select * from UserInformation where email = '%s'"%email
    db.ping(reconnect=True)
    cur.execute(sql)
 	result = cur.fetchone()
	if result is not None:
		flash("该Email已存在！")
 		return render_template('register.html')
except Exception as e:
	raise e
```
这里注册的用户类型我们肯定是不可以注册管理员的，不然这个管理员就是形同虚设了，我们这里通过register页面来注册的用户，我们统一都是普通用户，这里type置为0。然后创建时间我们使用服务器端来获取当前的时间。这里要使用time库，需要导入
```python
import time
create_time = time.strftime("%Y-%m-%d %H:%M:%S")
```
然后将数据插入数据库中，同时在插入完成之后我们应该返回首页，并且为登录状态，由于我们这里首页和登录都还没有实现，所以这里我们先写一个空的首页路由，并且创建一个index.html，使用路由返回index.html页面。
index.html我们先这样空置，等在本讲的最后我们来实现这个首页。
index.html:
```html
{% extends 'base.html' %}

{% block title %}
主页
{% endblock %}

{% block css %}

{% endblock %}

{% block content %}

{% endblock %}
```
完成注册服务器端功能之后的app.py全部代码为：
```python
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
```

这样我们的注册功能就全部实现啦！可以先去注册一个自己的测试账号，方便我们后面的各项功能测试呦！

### 2.3 登录功能实现
下面我们就来实现登录功能
#### 2.3.1 登录功能实现-前端
登录的话，前端和我们的注册类似，上面一个页头，然后下面使用一个表单，并且设置一个block用来标记一下当前的页面即可，在注册的前端设计的时候已经有详细的说明，这里就不在赘述了,创建一个login.html，下面废话不过说，直接上代码：
首先我们在app.py中写一个空的路由，方便我们在前端页面中使用url_for来重定向页面:
```python
# 注册页面
@app.route('/login')
def login():
    return render_template('login.html')
```
然后我们创建一个login.css来设置页面的样式:
```css
#page_header{
    text-align: center;
}

.login_content{
    /*调整边距，调到相对中间的位置*/
    margin:10% 30%;
}

#login_butt{
    text-align: center;
}
```
login.html部分为：
```html
{% extends 'base.html' %}

{% block title %}
登录
{% endblock %}

{% block css %}
<link rel="stylesheet" href="/static/css/login.css">
{% endblock %}

{% block content %}
<div class="login_content">
    <div class="page-header" id="page_header">
      <h1>登录<small>Login</small></h1>
    </div>
    <div id="login_form">
        <form method="post">
            <span style=" font-size:20px;color: red" >
                {% for item in get_flashed_messages() %}
                {{ item }}
                {% endfor %}
            </span>
          <div class="form-group">
            <label for="exampleInputEmail1">Email address</label>
            <input type="email" class="form-control" name="email" id="exampleInputEmail1" placeholder="Email address">
          </div>
          <div class="form-group">
            <label for="exampleInputPassword1">密码</label>
            <input type="password" class="form-control" name="password" id="exampleInputPassword1" placeholder="密码">
          </div>
          <div id="login_butt">
              <button type="submit" class="btn btn-default">登录</button>
              <button type="button" class="btn btn-default" onclick="location.href='{{ url_for('register') }}'">注册</button>
          </div>
        </form>
    </div>
</div>
{% endblock %}

{% block login_class %}
active
{% endblock %}
```
在登录页面完成之后，我们同时修改一下导航条的内容，在base.html中，将首页的导航修改为：
```html
 <li class="{% block login_class %} {% endblock %}"><a href="{{ url_for('login') }}">登录</a></li>
```
如果不修改base的话，直接运行上面的html修改之后的页面会报错，因为在login.html中使用了{% block login_class %} {% endblock %}，这个是刚刚在base.html中添加的block，用于标记当前页面。

修改完成之后我们的登录页面效果为：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200328095026349.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)

#### 2.3.2 登录功能实现-后端
登录功能的后端我们主要分为两部分，一个是接受表单并验证表单信息的正确性，并进行反馈，第二部分就是登录状态的保持，下面我们将分这两部分来实现后端的功能。
#####  2.3.2.1 登录功能实现-后端-验证登录信息
这里同样的，我们登录的表单为了安全性，一般都使用POST来发送，这里先设置允许的请求方式。
```python
@app.route('/login',methods=['GET','POST'])
```
然后我们来获取前端的Email和密码：
```python
# 登录页面
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
```
然后为了防止出错，我们先验证数据的完整性：
```python
if not all([email,password]):
    flash("请将信息填写完整！")
    return render_template('login.html')
```
然后我们来验证密码是否正确，首先我们先从数据库中获取当前登录email的密码，并验证它，如果密码不存，则说明该用户不存在，即未注册，我们返回提示。如果密码存在，那么我就获取密码，然后使用check_password_hash()函数来验证它,如果密码正确，我们将用户名（即email）放入session中，方便我们下面进行实现登录状态保持的功能。
代码为：
```python
# 登录页面
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if not all([email,password]):
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
            if check_password_hash(result[0],password):
                session['email'] = email
                session.permanent = True
                return redirect(url_for('index'))
            else:
                flash("密码错误！")
                return render_template('login.html')
        except Exception as e:
            raise e

```
这样我们的登录的基本功能就实现了，大家可以去测试下，如果登录正常则会返回首页，如果登录失败则会显示各种各样的提示。下面我们就要实现登录的另一个功能，登录状态保持，我们登录之后如何让系统一直保持我们的登录状态呢？

#####  2.3.2.1 登录功能实现-后端-登录状态保持
要实现登录状态保持，我们这里可以使用上下文钩子函数来一直保持登录状态。
```python
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
                return {'email':email,'nickname':result[0] ,'user_type':result[1]}
        except Exception as e:
            raise e
    # 如果email信息不存在，则未登录，返回空
    return {}
```
有了登录状态保持之后，我们就可以再次的修改导航条，将右侧的注册登录进行修改，当未登录时，显示登录注册，当已登录的时候，显示注销和{ 用户昵称 }，用户昵称处我们可以使用下拉列表，等后期我们会在此添加功能。
修改之后的导航栏右面内容为：
```html
{% if email %}
    <li class="{% block login_out_class %}{% endblock %}"><a href="{{ url_for('register') }}">注销</a></li>
    <li class="dropdown">
      <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{{ nickname }} <span class="caret"></span></a>
      <ul class="dropdown-menu">
        <li><a href="#">Action</a></li>
        <li><a href="#">Another action</a></li>
        <li><a href="#">Something else here</a></li>
        <li role="separator" class="divider"></li>
        <li><a href="#">Separated link</a></li>
      </ul>
    </li>
{% else %}
    <li class="{% block register_class %}{% endblock %}"><a href="{{ url_for('register') }}">注册</a></li>
    <li class="{% block login_class %} {% endblock %}"><a href="{{ url_for('login') }}">登录</a></li>
{% endif %}
```
这样我们登录之后的页面效果为：![在这里插入图片描述](https://img-blog.csdnimg.cn/20200328102620212.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
为了防止小伙伴不知道上面的这段代码到底在哪里修改，这里再贴一下修改后的base.html的全部代码：这里的注销的链接还没有写，在等会我们实现了注销的功能之后再在这里添加链接。
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
                <li class="{% block homepage_class %}{% endblock %}"><a href="{{ url_for('index') }}">首页<span class="sr-only">(current)</span></a></li>
                <li><a href="#">Link</a></li>
                <li class="dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
                  <ul class="dropdown-menu">
                    <li><a href="#">Action</a></li>
                    <li><a href="#">Another action</a></li>
                    <li><a href="#">Something else here</a></li>
                    <li role="separator" class="divider"></li>
                    <li><a href="#">Separated link</a></li>
                    <li role="separator" class="divider"></li>
                    <li><a href="#">One more separated link</a></li>
                  </ul>
                </li>
              </ul>
              <form class="navbar-form navbar-left">
                <div class="form-group">
                  <input type="text" class="form-control" placeholder="Search">
                </div>
                <button type="submit" class="btn btn-default">Submit</button>
              </form>
              <ul class="nav navbar-nav navbar-right">
                {% if email %}
                    <li class=""><a href="{{ url_for('register') }}">注销</a></li>
                    <li class="dropdown">
                      <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{{ nickname }} <span class="caret"></span></a>
                      <ul class="dropdown-menu">
                        <li><a href="#">Action</a></li>
                        <li><a href="#">Another action</a></li>
                        <li><a href="#">Something else here</a></li>
                        <li role="separator" class="divider"></li>
                        <li><a href="#">Separated link</a></li>
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
    <div>
        {% block content %}
{#        其他页面重写页面内容的地方#}
        {% endblock %}
    </div>
</body>
</html>
```

### 2.4 注销功能实现
下面我们就来完成用户的注销功能，其实注销功能实现很简单，我们这里就简单粗暴的将session清空即可达到注销的效果,清空之后我们重定向到首页即可。
```python
# 用户注销
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for(('index')))
```

### 2.5 主页实现
其实这里排版有一点小小的失误，我们应该第一个实现首页的，不过现在实现也并不影响。首页我们需要的功能很简单，找个漂亮唯美的背景图，中间加上几个"在线论坛系统"大字即可，一个漂漂亮亮的首页就完成了，因为我们目前首页不需要别的功能在，暂时就设置这样子就好了，我们先去随便找一个唯美的风景图。我们这里在百度图库中随便找了一个，然后把它下载放到我们的/static/img文件中。然后在我们之前创建的index.html中插入这张图片，再创建一个index.css，对样式进行调整。
在插入之后我们发现图片和上面导航栏会有一点点的空隙，看着还不舒服。这里我们需要为base.html创建一个base.css来设置一下导航条的样式，为他设置height = 52px；这样会无缝衔接，这个值也可以稍微大一点。然后我们在base.html中引入样式。
```css
.navigation_bar{
    height: 52px;
}
```
```html
    <link rel="stylesheet" href="/static/css/base.css">
```
这样之后我们的图片就可以无缝衔接了。我们的图片是作为一个大的div背景图片插入的，这样方便我们在上面进行显示标题。下面直接贴代码：
index.html:
```html
{% extends 'base.html' %}

{% block title %}
主页
{% endblock %}

{% block css %}
<link rel="stylesheet" href="/static/css/index.css">
{% endblock %}

{% block content %}
<div class="index_content">
    <div class="index_title">
        <h1>在线论坛系统<small>Online Forum Platform</small></h1>
    </div>
</div>
{% endblock %}
```
index.css:
```css
.index_content{
    margin: 0;
    padding: 0;
    width: 100%;
    /*这里由于图片高为1200，所以直接设置了1200，大家可以可以根据自己的需求进行设置*/
    height: 1200px;
    background-image: url("/static/img/index.jpeg");
}
.index_title{
    text-align: center;
    padding: 20% 20%;
}
.index_title h1{
    font-style: italic;
    font-size: 60px;
    text-shadow: 0.15em 0.15em 0.1em #333;
    font-weight: bolder;
}
```

在app.py中，我们主页的路由暂时只需要返回页面即可：
```python
# 主页
@app.route('/')
def index():
    return render_template('index.html')
```
下面来让我们看一下主页的效果图：(博客直男审美，各位可以自己设计主页的效果)![在这里插入图片描述](https://img-blog.csdnimg.cn/20200328105953169.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
好了，第二讲就到这里，我们第三讲再见！第三讲我们将继续实现论坛的功能，该到了实现论坛真正功能的时候，这一讲主要是各个系统都通用的功能：导航条、登录、注册、注销、主页。
我们下棋见，如果觉得写得不过，给个点赞关注支持下博客，谢谢大家。