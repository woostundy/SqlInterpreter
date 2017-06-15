# -*- coding:utf-8 -*-
import re
from structure import Database, Table, Column


class SQLFileParser(object):
    def __init__(self, database_name, file_content):
        self.database_name = database_name
        self.file_content = file_content

    def get_db(self):
        table_pattern = r'CREATE TABLE([\s\S]*?);'
        pattern = re.compile(table_pattern)
        table_contents = re.findall(pattern, self.file_content)
        tables = []
        for content in table_contents:
            tables.append(self._get_tables(content))
        db = Database(name=self.database_name, tables=tables)
        return db

    def _get_tables(self, table_content):
        """
        :param table_content
        :return:
        """

        content_lines = table_content.split('\n')
        table_name_line = content_lines[0]
        name_pattern = r'.*?`(.*?)`.*?'
        name_result = re.match(name_pattern, table_name_line.strip())
        name = name_result.group(1) if name_result else ''

        table_comment_line = content_lines[-1]
        comment_pattern = r".*COMMENT='(.*?)'.*"
        comment_result = re.match(comment_pattern, table_comment_line)
        comment = comment_result.group(1) if comment_result else ''

        column_lines = content_lines[1:-1]
        return Table(name=name, comment=comment, columns=self._get_columns(column_lines))

    def _get_columns(self, column_lines):
        """
        :param column_lines:
        :return:columns
        """
        columns = []
        for column_line in column_lines:
            column_info = column_line.strip().split(' ')
            column_name_result = re.match(r'`(.*?)`', column_info[0])
            if column_name_result:
                # 列名
                name = column_name_result.group(1)

                # 列属性
                type_info = re.match(r'(.*)\((.*)\)', column_info[1])
                if type_info:
                    _type = type_info.group(1)
                    length = type_info.group(2)
                else:
                    # 没长度时的情况
                    _type, length = column_info[1], ''

                # 列备注
                column_comment_result = re.match(r'.*?COMMENT \'(.*?)\'.*?', column_line.strip())
                if column_comment_result:
                    comment = column_comment_result.group(1)
                else:
                    comment = column_info[-1]
                    if '\'' in comment:
                        comment = comment.replace('\'', '')
                column = Column(name, comment, _type, length)
                columns.append(column)
        return columns
