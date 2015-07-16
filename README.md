# LouCloud
仿OpenStack云计算管理软件


#基本功能
1. 用户管理：管理员，普通用户。整个系统只有一个管理员，管理员在系统初始化时创建，普通用户由管理员创建。
2. 服务器管理：可以添加、删除服务器到资源池，支持多台服务器的管理
3. 镜像管理：镜像的添加和删除。镜像用来创建虚拟机的磁盘，是一个已经装好系统同时做了一定配置的特殊磁盘
4. 虚拟机模板管理：虚拟机模板定义了基于此模板创建的虚拟机的基本配置信息，比如虚拟机拥有多少个 CPU，多少内存以及使用哪个镜像。
5. 虚拟机管理：虚拟机的创建，启动，关闭，重启，删除操作。
6. 配置管理：系统的一些配置信息，比如新用户默认设置等。


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


#代码结构
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
