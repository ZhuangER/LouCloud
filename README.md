# LouCloud
仿OpenStack云计算管理软件


#基本功能
1. 用户管理：管理员，普通用户。整个系统只有一个管理员，管理员在系统初始化时创建，普通用户由管理员创建。
2. 服务器管理：可以添加、删除服务器到资源池，支持多台服务器的管理
3. 镜像管理：镜像的添加和删除。镜像用来创建虚拟机的磁盘，是一个已经装好系统同时做了一定配置的特殊磁盘
4. 虚拟机模板管理：虚拟机模板定义了基于此模板创建的虚拟机的基本配置信息，比如虚拟机拥有多少个 CPU，多少内存以及使用哪个镜像。
5. 虚拟机管理：虚拟机的创建，启动，关闭，重启，删除操作。
6. 配置管理：系统的一些配置信息，比如新用户默认设置等。

## 用户管理
###用户角色
- 管理员
- 普通用户

###添加用户
###删除用户
###更新用户
###用户更新配置

##服务器管理
###添加服务器
###删除服务器

##2.3 镜像管理

###2.3.1 添加镜像

输入镜像的路径及名称，添加到 LouCloud 系统中。

###2.3.2 删除镜像

在 LouCloud 系统中删除镜像记录，但不会在服务器上删除。

##2.4 模板管理

###2.4.1 添加模板

输入模板的基本配置，添加到 LouCloud 系统中。

###2.4.2 删除模板

在 LouCloud 系统中删除模板。

###2.4.3 更新模板

更新模板的基本配置。

##2.5 虚拟机管理

###2.5.1 创建

选择模板，输入虚拟机名称，创建虚拟机。

###2.5.2 删除

删除虚拟机。

###2.5.4 开机

启动虚拟机。

###2.5.5 关机

关闭虚拟机。

###2.5.6 重启

重启虚拟机。

###2.5.7 连接虚拟机

通过 Web 桌面的方式连接虚拟机。

##2.6 配置管理

添加系统所需的配置信息，比如用户虚拟机配额等。

综上，这就是我们6星期内要完成的产品需求，如果有任何不清楚的地方，请随时点击实验文档下方的课程问答发起提问。

#涉及到的技术
- 操作系统：Linux 基本操作
- 编程语言：Python 语言开发
- 开发框架：Flask Web 框架，MVC 开发模式
- 虚拟化技术： KVM/QEMU，Libvirt API 接口开发
- 云计算技术：基础设施即服务（IaaS）基本概念
- 数据库：MySQL 数据库设计及 SQLAlchemy 接口开发
- 开发流程：Git 基本操作及代码库使用
- 安装部署：Virtualenv，Apache，WSGI等
- 前端开发：Bootstrap 3.0，HTML，Javascript

# 技术架构
整个项目的知识点比较集中，Web 开发+虚拟化开发。底层为 MySQL 数据库与QEMU 虚拟化，中间层的接口分别为 Flask-SQLAlchemy 及 Libvirt API。上层 Flask Web开发框架。

# 开发环境搭建

## 安装virtualenv
```bash
sudo apt-get update
sudo apt-get install python-virtualenv
```

##安装虚拟化相关组件
```bash
# 安装虚拟化组件
sudo apt-get install qemu libvirt-bin python-libvirt
# 启动 libvirt-bin 服务
sudo service libvirt-bin start
# 查看 libvirt-bin 服务状态
sudo service libvirt-bin status
# 查看当前虚拟机列表，具体可使用virsh --help 帮助命令
sudo virsh list
```

## MySQL相关组件
```bash
sudp apt-get install mysql-server
```

## Flask及相关扩展
Flask：Flask 框架基础包
Flask-SQLAlchemy：在 Flask 中使用的 SQLALchemy ORM，用于数据库操作；
Flask-WTF：页面表单扩展；
Flask-Cache：缓存扩展；
Flask-Login：用户登陆认证及会话管理组件；
Flask-Script：Flask 的脚本支持，例如 manage.py 这类启动和管理脚本；

安装扩展包
```bash
pip install -r requirement.txt
```


#代码结构
```
|-- README.md
|-- loucloud
|   |-- __init__.py
|   |-- app.py
|   |-- config.py
|   |-- extension.py
|   |-- static
|   |-- templates
|   `-- user
|       |-- __init__.py
|       `-- views.py
`-- manage.py
```

# virsh常用命令
```
命令               说明
help            显示该命令的说明
quit            结束 virsh，回到 Shell
connect            连接到指定的虚拟机服务器
create            启动一个新的虚拟机
destroy            删除一个虚拟机
start            开启（已定义的）非启动的虚拟机
define            从 XML 定义一个虚拟机
undefine        取消定义的虚拟机
dumpxml            转储虚拟机的设置值
list            列出虚拟机
reboot            重新启动虚拟机
save            存储虚拟机的状态
restore            回复虚拟机的状态
suspend            暂停虚拟机的执行
resume            继续执行该虚拟机
dump            将虚拟机的内核转储到指定的文件，以便进行分析与排错
shutdown        关闭虚拟机
setmem            修改内存的大小
setmaxmem       设置内存的最大值
setvcpus        修改虚拟处理器的数量
```
