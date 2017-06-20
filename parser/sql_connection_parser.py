# -*- coding:utf-8 -*-
import re
from structure import Database, Table, Column
from sqlalchemy import inspect, create_engine
from sqlalchemy.orm import sessionmaker


class SQLConnectionParser(object):
    def __init__(self, database_name, connection, charset='utf8'):
        if '://' not in connection:
            connection = 'mysql://' + connection
        connection = connection + '?charset=' + charset
        self.engine = create_engine(connection, encoding='utf-8')
        self.database_name = database_name
        self.schema_name = None

    def get_db(self):
        inspector = inspect(self.engine)
        if not inspector.default_schema_name:
            raise ValueError('You must appoint the database')
        elif not self.database_name:
            self.database_name = inspector.default_schema_name
        elif not inspector.default_schema_name:
            self.schema_name = self.database_name

        tables = []
        for table_name in inspector.get_table_names():
            comment = inspector.get_table_options(table_name).get('mysql_comment')
            if comment:
                comment = comment.encode('utf-8')
            table = Table(table_name.encode('utf-8'), comment, self._get_columns(table_name))
            tables.append(table)
        db = Database(self.database_name, tables)
        return db

    def _get_columns(self, table_name):
        # 这里不用 inspector.get_columns() 是因为 SqlAlchemy 1.2 以下的版本里column没有comment的属性
        session = sessionmaker(bind=self.engine)()
        column_result = session.execute('show full fields from {0};'.format(table_name)).fetchall()
        columns = []
        for i in column_result:
            # 列属性
            type_info = re.match(r'(.*)\((.*)\)', i['Type'])
            if type_info:
                _type = type_info.group(1)
                length = type_info.group(2)
            else:
                # 没长度时的情况
                _type, length = i['Type'], ''

            column = Column(i['Field'].encode('utf-8'), i['Comment'].encode('utf-8'), _type, length)
            columns.append(column)
        return columns


if __name__ == '__main__':
    parser = SQLConnectionParser('wc_open', 'root:k@10.180.55.112/wc_open')
    print parser.get_db()
