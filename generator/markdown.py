# -*- coding: utf-8 -*-
from template.markdown_template import table_header_template, md_template
from generator.common import mk_dir, PASS_KEY


def gen_md(database):
    """
    输出markdown 文档
    :param database:
    :return:
    """
    pth = mk_dir(database.name, 'markdown')
    md_content = md_template.format(database_name=database.name)
    for table in database.tables:
        table_content = '\n'.join('|{name}|{type}|{length}|{comment}|'.format(**vars(column))
                                  for column in table.columns if column.name not in PASS_KEY)
        table_section = table_header_template.format(table_name=table.name, table_comment=table.comment) + table_content
        md_content += table_section
    with open(pth + '/' + database.name + '.md', 'w') as f:
        f.write(md_content)
