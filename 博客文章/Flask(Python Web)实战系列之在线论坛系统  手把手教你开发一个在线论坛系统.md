## Flask(Python Web)实战系列之在线论坛系统 一
本系列博客将手把手带你进行开发一个在线论坛系统，全程记录一个Python Web开发的全过程，服务端使用Python Web的Flask框架进行开发，数据库采用MySQL，前端采用HTML/CSS/JavaScript/Bootstrap来进行开发。使用Pycharm进行开发，最后会有部署到Linux服务器的教程系列。这个这个项目源码在GitHub上进行开源，本项目的GitHub地址为：[OnlineForumPlatform](https://github.com/qiguanjie/OnlineForumPlatform),大家可以去clone全部源码，喜欢的话，也欢迎大家star一下。
   如果对Flask还没学习过的同学，可以看我之前的一篇Flask博客，一年多前写的了，写的不是太好，但是总体顺序还是能够看懂Flask是如何运行的，可以进行上手，博客地址为：[Flask学习（一）博客地址](https://blog.csdn.net/qq_43422111/article/details/104304290)
   如果对BootStrap不会使用的同学可以看我前几天的博客，有Bootstrap手把手教学，让你快速上手使用BootStrap，博客地址为：[一文教会你Bootstrap，让你也可以快速建站](https://blog.csdn.net/qq_43422111/article/details/105098288)
    本次的项目是一个在线论坛系统，字如其名，就是开发一个在线的论坛系统。分为普通用户和管理员两个端，普通用户。需要实现的功能如下：

-   注册：注册账号
-   登录：登录账号进入系统，如果登录普通用户，则只有普通用户的权限，如果是管理员账号，则有管理员账号权限。
-   查看论坛问题列表：查看在线论坛系统中所有已发布的问题.
-   发布问题：
    -   发布自己的问题，等待他人回答
    -   支持富文本输入
    -   支持Markdown输入
-   问题详情页面：显示当前问题的讨论、回复。
-   回答问题：回答他人问题。
-   个人中心：
    -   显示个人账号信息
    -   可以修改个人账号信息
    -   显示个人发帖情况
    -   显示个人回复情况

暂定功能为这些：本项目基本预期耗时五天进行开发，同时进行博客更新。话不多说，下面我们就开始吧！
### 1.1 首先创建项目
这里使用Pycharm专业版作为开发工具，如果还没有Pycharm的同学可以下载安装一个，如果没有激活的话，可以查看[一文教你如何白嫖JetBrains全家桶（IDEA/PtChram/CLion）免费正版](https://blog.csdn.net/qq_43422111/article/details/105128206)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200327145750710.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
这里选择Flask项目，我这里的项目名称为OnlineForumPltform，使用virtualenv虚拟环境，模板引擎为Jinja2。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200327145801397.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
这样一个Flask基本项目就创建好啦。创建完成之后页面为这样：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200327145813289.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
我们点击运行，测试一下第一个hello world：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200327145827445.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
运行之后，我们访问运行栏中的地址，默认的地址为:http://127.0.0.1:5000
页面返回Hello World!就表示我们第一个已经完成了第一步！
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020032714583921.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
下面我们来创建一些我们下面开发所需要的文件和文件夹。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200327145847137.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
还有requirements.txt文件是存放本项目所有插件和版本信息的文本，README.md文件是本项目的说明文件。

### 1.2 安装本项目所需要的一些插件


点开设置，进行安装插件：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200327145908626.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
点击+进入添加插件页面，这里我们先添加一个PyMysql，其他的等我们需要的时候再进行添加。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200327145918689.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)

### 1.3 创建数据库
这里我们先创建一个空的数据库，然后我们使用PyCharm连接这个数据库，方便我们后面进行数据库相关的操作。
（我这里是mac系统，mysql只安装了命令行版本，如果是安装图像界面版本的可以直接进行创建）.终端进入mysql的命令为`mysql -u root -p `然后输入密码即可进入。
```bash
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.16 MySQL Community Server - GPL

Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> create database OnlineForumPlatform;
Query OK, 1 row affected (0.06 sec)

mysql>
```
即可创建成功。

创建完成之后我们使用PyChram来连接数据库。
![在这里插入图片描述](https://img-blog.csdnimg.cn/202003271459340.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
选择mysql数据库，然后我们填写用户名root和密码，然后填写创建的数据库名称即可，填写完成之后点击测试连接
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200327145950753.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
测试连接正确之后，我们点击OK即可
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200327150000745.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
然后我们在pycharm右面的Database就可以看到我们的数据库了
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200327150009100.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQzNDIyMTEx,size_16,color_FFFFFF,t_70)
