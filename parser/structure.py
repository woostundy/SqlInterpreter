# -*- coding: utf-8 -*-
from collections import namedtuple

Database = namedtuple('Database', ('name', 'tables'))
Table = namedtuple('Table', ('name', 'comment', 'columns'))
Column = namedtuple('Column', ('name', 'comment', 'type', 'length'))

