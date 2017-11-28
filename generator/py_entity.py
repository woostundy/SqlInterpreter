# -*- coding: utf-8 -*-
from generator.common import mk_dir, underline_to_camel, plural, PASS_KEY
from template.entity_template import py_entity
import os


def gen_py_entity(database, table_name=None):
    """
    输出 python的entity代码
    :param database:
    :param table_name:
    :return:
    """
    pth = mk_dir(database.name, 'py_entity')
    for table in database.tables:

        if table_name is not None and table_name != table.name:
            continue

        doc_string_list = []
        entity_property_list = []

        for col in table.columns:
            if col.name in PASS_KEY:
                continue
            doc_string_list.append(':param {0}: {1}'.format(col.name, col.comment))
            entity_property_list.append('self.{0} = kwargs.get(\'{0}\')'.format(col.name))

        # 拼接doc_string 和 实体属性
        doc_string = '\n\t'.join(doc_string_list).expandtabs()
        entity_properties = '\n\t'.join(entity_property_list).expandtabs()

        # 生成内容
        content = py_entity.format(
            entity_name=underline_to_camel(table.name),
            entity_comment=table.comment,
            doc_string=doc_string,
            entity_properties=entity_properties
        )
        with open(pth + '/' + plural(table.name) + '.py', 'w') as f:
            f.write(content)

    print 'entity files have output to ', os.path.abspath('.'), '/output/py_entity/'
