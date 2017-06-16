# SQLInterpreter
SQLInterpreter 输入.sql文件或者数据库连接，输出数据库文档或者模板代码

目前支持的输出结果:

- [x] Python 实体模板代码
- [x] Markdown 数据库文档
- [ ] Word 数据库文档
- [ ] HTML 数据库文档

目前支持的输入类型:

- [x] .sql 文件
- [ ] sql数据库连接

目前支持的数据库类型:

- [x] MySQL
- [ ] MS SQL SERVER

咋用：

python interpreter.py -f database.sql

更多参数详情见 python interpreter.py -h