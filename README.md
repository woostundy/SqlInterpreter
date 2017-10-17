# SQLInterpreter
SQLInterpreter 输入.sql文件或者数据库连接，输出数据库文档或者模板代码

目前支持的输出结果:

- [x] Python 实体模板代码
- [x] Markdown 数据库文档
- [ ] Word 数据库文档
- [ ] HTML 数据库文档

目前支持的输入类型:

- [x] .sql 文件
- [x] sql数据库连接

目前支持的数据库类型:

- [x] MySQL
- [ ] MS SQL SERVER

咋用：

`python interpreter.py -f sample.sql`
`python interpreter.py -c user:pwd@host/sample_db` -t table_name

更多参数详情见 `python interpreter.py -h`

样例效果

Markdown
![Markdown Doc][1]

Python Entity
![Python Entity][2]


  [1]: http://7xlizz.com1.z0.glb.clouddn.com/699B4817-1284-494D-9F50-098B439BD115.png
  [2]: http://7xlizz.com1.z0.glb.clouddn.com/ADF7C484-2F10-48A3-9871-984E11A8EEB6.png