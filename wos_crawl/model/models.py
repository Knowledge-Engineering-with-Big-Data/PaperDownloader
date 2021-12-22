#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/2 11:22
# @Author : ZhangXiaobo
# @Software: PyCharm
from sqlalchemy import Column, Text, Integer,Boolean

from . import Base

#
# class CrawlerStates(Base):
#     __tablename__ = 'crawler_states'
#     uniqueid = Column(Text, primary_key=True)
#     doi = Column(Text)
#     year = Column(Integer)
#     state = Column(Boolean)
#
# def __repr__(self):
#     return 'id:{}，doi:{},year:{}'.format(self.uniqueid,self.doi,self.year)

class CrawlerStates(Base):
    __tablename__ = 'crawlerstates'
    uniqueid = Column(Text,primary_key=True)
    doi = Column(Text)
    state = Column(Boolean)

def __repr__(self):
    return 'id:{}，doi:{},year:{}'.format(self.uniqueid,self.doi,self.year)