# -*- coding: utf-8 -*-
import argparse
import os

from parser.sql_file_parser import SQLFileParser
from generator import gen_py_entity, gen_md


def init_args():
    parser = argparse.ArgumentParser(description='-- SQL Interpreter --')
    method_group = parser.add_mutually_exclusive_group()
    method_group.add_argument('-c', '--connection', help='interpreter by sql connection', nargs=1, dest='connection')
    method_group.add_argument('-f', '--file', help='interpreter by .sql file', dest='file_path')
    method_group.required = True

    parser.add_argument('-o', '--output', help='the files you want to output', nargs='+',
                        choices=['md', 'py', 'word'], default=['md', 'py', 'word'], dest='output')
    parser.add_argument('-db', '--database', help='db name, if you don\'t appoint it, it will be the file name',
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
        raise ValueError("Numbered Mode")

    output_map = {
        # 暂不支持的就返回个0吧。。。
        'py': gen_py_entity,
        'word': lambda x: 0,
        'md': gen_md,
    }
    for v in output:
        output_map[v](database)


if __name__ == '__main__':
    options = init_args()
    main(**vars(options))
