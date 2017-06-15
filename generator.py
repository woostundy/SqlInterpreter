# -*- coding: utf-8 -*-
import os
from template.entity_template import py_entity
from template.markdown_template import table_header_template, md_template
from helper import underline_to_camel, plural

PASS_KEY = [
    'id',
    'created',
    'modified',
]


def gen_py_entity(database):
    """
    输出 python的entity代码
    :param database:
    :return:
    """
    pth = _mk_dir(database.name, 'py_entity')
    for table in database.tables:
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


def gen_md(database):
    """
    输出markdown 文档
    :param database:
    :return:
    """
    pth = _mk_dir(database.name, 'markdown')
    md_content = md_template.format(database_name=database.name)
    for table in database.tables:
        table_content = '\n'.join('|{name}|{type}|{length}|{comment}|'.format(**vars(column))
                                  for column in table.columns if column.name not in PASS_KEY)
        table_section = table_header_template.format(table_name=table.name, table_comment=table.comment) + table_content
        md_content += table_section
    with open(pth + '/' + database.name + '.md', 'w') as f:
        f.write(md_content)


def _mk_dir(db_name, dir_name):
    if not os.path.exists('output/' + db_name):
        os.mkdir('output/' + db_name)
    pth = os.path.join('output', db_name, dir_name)
    if not os.path.exists(pth):
        os.mkdir(pth)
    return pth


if __name__ == '__main__':
    print underline_to_camel('ab_cde')
