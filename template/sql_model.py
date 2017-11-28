# -*- coding: utf-8 -*-

sql_base = """# -*- coding: utf-8 -*-
# created by SQLInterpreter
import sys

import config
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

reload(sys)
sys.setdefaultencoding('utf8')

Base = automap_base()

database = create_engine(config.MYSQL_CONN, pool_recycle=120)

# 默认自动flush（一旦flush就能在query中拿到数据），但是不自动提交（不提交就不会真的写到数据库中去），
# 由程序自己控制，这样有利于事务的控制
DBSession = sessionmaker(bind=database, autoflush=True, autocommit=False, expire_on_commit=True)


def get_session():
    return DBSession()
    
"""
sql_model_string = """
class {entity_name}Model(Base):
    __tablename__ = '{table_name}'

"""