# -*- coding: utf-8 -*-
import argparse
import os

from parser.sql_file_parser import SQLFileParser
from parser.sql_connection_parser import SQLConnectionParser
from generator.py_entity import gen_py_entity
from generator.markdown import gen_md


def init_args():
    parser = argparse.ArgumentParser(description='-- SQL Interpreter --',
                                     usage='\ninterpreter -c mysql://user:pwd@host/db -o py'
                                           '\ninterpreter -f sample.py -name sample_db -o md,py'
                                           '\ninterpreter -c user:pwd@host/sample_db')
    method_group = parser.add_mutually_exclusive_group()
    method_group.add_argument('-c', '--connection', help='interpreter by sql connection', dest='connection')
    method_group.add_argument('-f', '--file', help='interpreter by .sql file', dest='file_path')
    method_group.required = True

    parser.add_argument('-o', '--output', help='the files you want to output', nargs='+',
                        choices=['md', 'py', 'word', 'html'], default=['md', 'py', 'word', 'html'], dest='output')
    parser.add_argument('-name', '--dbname', help='db name, if you don\'t appoint it, it will be the file name',
                        dest='db_name', default=None)
    result = parser.parse_args()
    return result


def main(file_path, connection, output, db_name):
    database = None
    if file_path:
        # 从文件解析DB
        with open(file_path, 'r') as f:
            if not db_name:
                base_name = os.path.basename(file_path)
                db_name = os.path.splitext(base_name)[0]
            content = f.read()

        file_parser = SQLFileParser(db_name, content)
        database = file_parser.get_db()
    if connection:
        connection_parser = SQLConnectionParser(db_name, connection)
        database = connection_parser.get_db()

    output_map = {
        # 暂不支持的就返回个0吧。。。
        'py': gen_py_entity,
        'word': lambda x: 0,
        'md': gen_md,
        'html': lambda x: 0
    }
    for v in output:
        output_map[v](database)


if __name__ == '__main__':
    options = init_args()
    main(**vars(options))
