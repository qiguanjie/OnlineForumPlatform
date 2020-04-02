> 大家好，我叫亓官劼（qí guān jié ）,这个《小白都能看懂的实战教程 手把手教你Python Web全栈开发》是一个零基础的实战教程，手把手带你开发一套系统，带你了解Python web全栈开发，目前正在连续更新中，如果喜欢的话可以点赞关注博主，后面会持续更新。

[博客文章内容导航（实时更新）](https://blog.csdn.net/qq_43422111/article/details/105174460)
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

本项目所有源码在GitHub开源，GitHub地址为：[OnlineForumPlatform](https://github.com/qiguanjie/OnlineForumPlatform)有需要源码可以前去查看，喜欢的话可以star一下

## 小白都能看懂的实战教程 手把手教你Python Web全栈开发  DAY 5
&emsp;&emsp;今天来到我们实战系列的第五天，在之前的四天里，我们已经完成了在线论坛系统的导航条、登录、注册、论坛页面、帖子详情页面等的功能实现，目前我们的论坛已经可以进行帖子发布，查看帖子详情，并且进行回复信息了。在上一讲中，我们还是先了功能限制，对不同用户的访问进行过滤。下面我们继续来完善我们的这个在线论坛系统，今天我们来完善我们的在线论坛系统的个人中心。

### 5.1个人中心页面实现
&emsp;&emsp;今天我们就来实现我们的个人中心页面，这里本来是打算使用AJAX实现的，个人中心使用AJAX实现的话，可以使得整体不变，当我们点击各个分栏的时候只返回各个分栏的信息，是一个非常好的选择。但是由于这个系列打算让每一个看的人都能够看懂，实现这个功能，所以我们这简化一点，直接使用普通的一个请求页面。后面有兴趣的同学可以进行进一步的优化，后面有空的话，我也会将后面逐渐优化的教程发出来。
#### 5.1.1 个人中心页面-后端
&emsp;&emsp;那我们就开始实现我们我的个人中心了，这里我们的个人中心只显示我们的一些基础资料（我们也没设置多少），这里只做一个大致的样式展示，更多的功能我们后续慢慢的进行一个拓展。
&emsp;&emsp;我们去看了一下我们的数据库，发现我们个人中心能够进行展示的，也就只有我们的email、昵称、用户类型、创建时间和手机号码可以进行一个展示和修改。那我们就展示这么多吧，大家也可以添加一下个性签名，头像等一系列的个人标识进入数据库中。
&emsp;&emsp;那我们就开始获取我们的数据了，首先我们需要限制只有登录的用户才可以进入到我们的个人中心，限制的方法在上一讲中已经实现了。
```python
# 个人中心
@app.route('/personal')
@login_limit
def personal():
    if request.method == 'GET':
        email = session.get('email')
        try:
            cur = db.close()
            sql = "select email, nickname, type, create_time, phone from UserInformation where email = '%s'" % email
            db.ping(reconnect=True)
            cur.execute(sql)
            personal_info = cur.fetchone()
        except Exception as e:
            raise e
        return render_template('personal.html',personal_info = personal_info)
```

#### 5.1.2 个人中心页面-前端
&emsp;&emsp;在后端获取完数据之后，我们在前端对获取到的数据进行展示即可。所以我们先设计个勉强能够看得过去的架子，来展示我们的数据。先上个效果图吧：![在这里插入图片描述](https://img-blog.csdnimg.cn/20200401142929971.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
确实是比较简陋的，但是功能齐全吧。我们这里使用的是`<table>`标签进行显示的，也可以使用`<li>`进行显示。这里时间上代码吧，personal.html的代码为：
```html
{% extends 'base.html' %}

{% block title %}
个人中心
{% endblock %}

{% block css %}
<link rel="stylesheet" href="/static/css/personal.css">
{% endblock %}

{% block content %}
<div class="personal_content">
    <div class="page-header" id="page_header">
      <h1>个人中心<small>Personal center</small></h1>
    </div>
    <div class="personal_info">
        <table>
            <tr class="personal_tr">
                <td class="personal_td">
                    Email address:
                </td>
                <td class="personal_td">
                    {{ personal_info[0] }}
                </td>
            </tr>
            <tr class="personal_tr">
                <td class="personal_td">
                    昵称：
                </td>
                <td class="personal_td">
                    {{ personal_info[1] }}
                </td>
            </tr>
            <tr class="personal_tr">
                <td class="personal_td">
                    注册时间：
                </td>
                <td class="personal_td">
                    {{ personal_info[3] }}
                </td>
            </tr>
            <tr class="personal_tr">
                <td class="personal_td">
                    手机号：
                </td>
                <td class="personal_td">
                    {{ personal_info[4] }}
                </td>
            </tr>
            <tr class="personal_tr">
                <td class="personal_td">
                    用户类型：
                </td>
                <td class="personal_td">
                    {% if personal_info[2] == 0 %}
                        普通用户
                    {% else %}
                        管理员
                    {% endif %}
                </td>
            </tr>
        </table>
    </div>
</div>
{% endblock %}
```
personal.css代码为：
```css
.personal_content{
    margin-left: 20%;
    margin-right: 20%;
    margin-top: 5%;
}
#page_header{
    text-align: center;
}

.personal_info{
    font-size: 24px;
    margin-left: 10%
;
}

.personal_td{
    width: 300px;
}

.personal_tr{
    height: 50px;
}
```
同时这里也修改了base.html的内容，我们让个人中心在下拉列表中进行显示，我们修改了下拉列表中第一个值和链接，效果图为：![在这里插入图片描述](https://img-blog.csdnimg.cn/20200401143136870.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
这里的修改的代码为：
```html
<li class="dropdown">
                      <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{{ nickname }} <span class="caret"></span></a>
                      <ul class="dropdown-menu">
                        <li><a href="{{ url_for('personal') }}">个人中心</a></li>
                        <li><a href="#">Another action</a></li>
                        <li><a href="#">Something else here</a></li>
                        <li role="separator" class="divider"></li>
                        <li><a href="#">Separated link</a></li>
                      </ul>
                    </li>
```

### 5.2 修改密码功能实现
&emsp;&emsp;到这里我们来实现我们的修改密码功能，其实如果使用AJAX实现的话，这一讲的所有功能都应该在个人中心一个页面中进行体现的，我们这里就先这样分开实现吧。大家可以自行改进~
&emsp;&emsp;在这里我们就先从前端开始实现了。
#### 5.2.1 修改密码功能实现-前端
&emsp;&emsp;我们修改密码的话，这里采用一个简单的验证，就是知道我们当前的密码就可以进行一个修改密码。我们设计一个表单，分别输入旧密码，新密码，确认新密码即可。先上个效果图再说实现：![在这里插入图片描述](https://img-blog.csdnimg.cn/20200401150530790.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
&emsp;&emsp;这效果图还是大家熟悉的味道，有没有！我们这里还是一个简单的div，里面加个页头，下面3个`input`。这里和前面的原理一样，这里我们预留了一个flash传输消息的地方，用于等会后端向前面传递消息提示，我们就直接上代码吧：
change_password.html:
```html
{% extends 'base.html' %}

{% block title %}
修改密码
{% endblock %}

{% block css %}
<link rel="stylesheet" href="/static/css/change_password.css">
{% endblock %}

{% block content %}
<div class="change_password_content">
    <div class="page-header" id="page_header">
      <h1>修改密码<small>Change Password</small></h1>
    </div>
    <div class="change_password_div">
        <form method="post">
            <span style=" font-size:20px;color: red" >
                {% for item in get_flashed_messages() %}
                {{ item }}
                {% endfor %}
            </span>
            <div class="form-group">
                <label for="exampleInputPassword1">旧密码：</label>
                <input type="password" class="form-control" name="old_password" id="exampleInputPassword1" placeholder="密码">
            </div>
            <div class="form-group">
                <label for="exampleInputPassword1">新密码：</label>
                <input type="password" class="form-control" name="new_password1" id="exampleInputPassword1" placeholder="密码">
            </div>
            <div class="form-group">
                <label for="exampleInputPassword1">确认密码：</label>
                <input type="password" class="form-control" name="new_password2" id="exampleInputPassword1" placeholder="密码">
            </div>
            <div id="password_butt">
              <button type="submit" class="btn btn-default">修改密码</button>
          </div>
        </form>
    </div>
</div>
{% endblock %}
```
change_paasword.css:
```css
#page_header{
    text-align: center;
}
.change_password_content{
    margin-left: 20%;
    margin-right: 20%;
    margin-top: 8%;
}
#password_butt{
    text-align: center;
}
```
#### 5.2.1 修改密码功能实现-后端
&emsp;&emsp;下面我们来实现修改密码的后端功能，使他能够正确的修改密码。我们首先获取我们的当前登录用户的用户名，这里我们的修改密码的功能也是只有我们登录的用户才可以访问的功能。首先我们判断是不是3个数据都获取到了，并且2个密码一致，如果有错误，我们返回提示。如果数据都正确的话，我们开始处理，先获取我们的email。我们获取到email之后去数据库中查找我们的密码，这里的密码是加密的，所以我们要使用check_password_hash()来进行验证，如果旧密码是正确的，我们就进行修改新密码，如果不正确，则返回。完整的后端代码为：
```python
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
```
在实现后端功能之后，我们可以再导航栏中加入修改密码的导航，我们还是加载下来列表中，将第二个修改为修改密码。
```html
<li class="dropdown">
  <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{{ nickname }} <span class="caret"></span></a>
  <ul class="dropdown-menu">
    <li><a href="{{ url_for('personal') }}">个人中心</a></li>
    <li><a href="{{ url_for('change_password') }}">修改密码</a></li>
    <li><a href="#">Something else here</a></li>
    <li role="separator" class="divider"></li>
    <li><a href="#">Separated link</a></li>
  </ul>
</li>
```
效果为：![在这里插入图片描述](https://img-blog.csdnimg.cn/20200401152411469.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)

### 5.3 查看发布帖子功能实现-后端
#### 5.3.1 查看发布帖子功能实现-后端

&emsp;&emsp;下面我们来实现个人中心的另一个功能，就是查看我们自己所发布的所有的帖子信息，并且可以在此页面进入到我们所发布的帖子中去。这里我们还是先写后端，向前端去传输我们的数据。这个页面是也是需要我们登录才可以查看的，因为查看的是我们所登录的这个账号所发布的帖子列表。
&emsp;&emsp;所以这里我们先获取我们需要的数据，然后把它返回到前端即可，这里先创建一个前端的html文件，这里使用show_issue.html，我们后端的代码为：
```python
# 查看已发布的帖子
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
```
#### 5.3.2 查看发布帖子功能实现-前端
&emsp;&emsp;下面我们开始实现前端的一个功能，我们这里使用和论坛列表相似的功能，我们这里只需要显示帖子的标题即可。这里先上效果图：![在这里插入图片描述](https://img-blog.csdnimg.cn/20200401160739120.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
我们这里只需要设计一个`<li>`将我们后端发送的数据仅显示出来即可。show_issue.html：
```html
{% extends 'base.html' %}

{% block title %}
已发布的帖子
{% endblock %}

{% block css %}
<link rel="stylesheet" href="/static/css/show_issue.css">
{% endblock %}

{% block content %}
<div class="show_issue_content">
    <div class="page-header" id="page_header">
        <h1>已发布的帖子列表</h1>
    </div>
    <div class="issue_list_div">
        <ul class="issue_list_ul">
            {% for issue in issue_detail %}
                <li class="issue_list_li">
                    <div class="issue_div">
                        <div class="issue_content">
                            <h3>
                                <a href="{{ url_for('issue_detail',Ino = issue[0]) }}">
                                    {{ issue[2] }}
                                </a>
                            </h3>
                        </div>
                        <div class="author_info">
                            <p class="post-info">
                                <span>发布时间：{{ issue[3] }}</span>
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
show_issue.css:
```css
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
    max-height: 200px;
}
.show_issue_content{
    margin-right: 20%;
    margin-left: 20%;
    margin-top: 8%;
}
```
这里我们也修改一下base.html文件，设置下来列表。![在这里插入图片描述](https://img-blog.csdnimg.cn/20200401161015987.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
我们在导航栏的下拉列表中添加我们这章个人中心的三个页面，这里贴一下目前base.html的全部代码，防止有的小伙伴找不到修改的地方。
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
