'''
目录权限
chown -R www-data:www-data .
chmod a+w .


软件安装
服务器上的准备工作（登录终端，安装软件）
登录putty，，出现一个终端画面，登录以后
就在终端输入apt-get update，回车，等待安装完后
输入apt-get upgrade，回车，等待安装完后，
输入apt-get install curl，回车，等待安装完后，
输入apt-get install python3 python3-pip apache2 zsh git libapache2-mod-wsgi-py3，回车，等待安装完后
输入pip3 install flask flask-sqlalchemy，回车，等待安装完后
输入sh -c "$(curl -fsSL  HYPERLINK "https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"，回车


wsgi文件
然后wsgi里面的内容是:
#!/usr/bin/env python3

import sys
from os.path import abspath
from os.path import dirname


sys.path.insert(0, abspath(dirname(__file__)))


from app import init_app
application = init_app()

# from app import app as application


服务器上修改配置
nano /etc/apache2/sites-enabled/000-default.conf


重启Apache
/etc/init.d/apache2 restart


查看 Apache 错误文档
cat /var/log/apache2/error.log

'''