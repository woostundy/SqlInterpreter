# -*- coding: utf-8 -*-
from generator.common import mk_dir, underline_to_camel, plural, PASS_KEY
from template.sql_model import sql_base, sql_model_string
import os


def gen_py_sql_model(database, table_name=None):
    """
    输出 python的entity代码
    :param database:
    :param table_name:
    :return:
    """
    pth = mk_dir(database.name, 'sql_model')
    content = sql_base
    for table in database.tables:

        if table_name is not None and table_name != table.name:
            continue

        # 生成内容
        content += sql_model_string.format(
            entity_name=underline_to_camel(table.name),
            table_name=table.name
        )

    with open(pth + '/' + plural(database.name) + '.py', 'w') as f:
        f.write(content)

    print 'sql_model file has output to ', os.path.abspath('.'), '/output/sql_model/'
