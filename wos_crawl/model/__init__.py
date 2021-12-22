#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/2 11:12
# @Author : ZhangXiaobo
# @Software: PyCharm
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


def get_engine(db_url=None, echo=False):
    """
    :param db_url: "mysql://user:password@localhost/mydatabase"
    :param echo:
    :return:
    """
    assert (db_url is not None)
    engine = create_engine(db_url, echo=echo)
    return engine


def get_session(engine, auto_flush=True):
    Session = sessionmaker(bind=engine, autoflush=auto_flush)
    session = Session()
    return session
