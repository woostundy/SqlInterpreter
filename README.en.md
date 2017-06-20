# SQLInterpreter
SQLInterpreter help you interpreting the .sql file to sample code or markdown doc.

Output support list:

- [x] Python Entity Code
- [x] Markdown Schema Doc
- [ ] Word Schema Doc
- [ ] HTML Schema Doc

Input support list:

- [x] .sql File
- [ ] Sql Connection

Database type support list:

- [x] MySQL
- [x] MS SQL SERVER

How to use：

`python interpreter.py -f sample.sql`
`python interpreter.py -c user:pwd@host/sample_db`

Type `python interpreter.py -h` for more params detail info


sample screenshot:

Markdown
![Markdown Doc][1]

Python Entity
![Python Entity][2]


  [1]: http://7xlizz.com1.z0.glb.clouddn.com/699B4817-1284-494D-9F50-098B439BD115.png
  [2]: http://7xlizz.com1.z0.glb.clouddn.com/ADF7C484-2F10-48A3-9871-984E11A8EEB6.png