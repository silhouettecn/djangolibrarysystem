## 图书管理系统

### 项目概要

这是数据库的期中project，设计并实现了一个精简的图书管理系统，具有图书入库、查询、借书、还书、借书证管理等功能。

实现方式：web网页。后端框架使用**django**(python)，连接**mysql**数据库（本地），前端使用**bootstrap**。

<br/>

### 运行项目

终端输入以下命令：

`python manage.py runserver 127.0.0.1:8000`

可打开网页：

http://127.0.0.1:8000/login/

<br/>

### 主要功能

* 登录

![landing](screenshots/landing.png)

<br/>

* 主页

![books](screenshots/books.png)


<br/>


* 图书查询
  - 可对书的类别, 书名, 出版社, 年份, 作者, 价格进行查询，支持多条件查询
  - 可按条件对图书进行排序

![search](screenshots/search.png)

<br/>

* 借书
  - 输入借书证卡号，显示该借书证所有已借书籍
  - 输入资产编号，如果该书还有库存，则借书成功，同时库存数减一；否则输出该书无库存，借书失败

![borrow](screenshots/borrow.png)

<br/>

* 还书（类似借书）
  - 输入借书证卡号，显示该借书证所有已借书籍 (返回, 格式同查询模块) 
  - 输入资产编号，如果该书在已借书籍列表内, 则还书成功, 同时库存加一；否则输出出错信息

<br/>

* 图书入库
  - 单本入库
  - 批量入库（支持csv）

![add](screenshots/add.png)

<br/>

* 借书证管理
  - 增加或删除一个借书证
  - note: 有未还书籍的借书证无法删除
  
<br/>
