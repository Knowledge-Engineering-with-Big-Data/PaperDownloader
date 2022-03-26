#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/3 20:53
# @Author : ZhangXiaobo
# @Software: PyCharm
from scrapy import cmdline
from wos_crawl.settings import FILES_STORE,DB_PATH
from wos_crawl.model.models import CrawlerStates
from wos_crawl.model import get_engine,get_session
import os

def updateToDb():
    pdf_list = os.listdir(FILES_STORE)
    engine = get_engine(db_url=DB_PATH)
    session = get_session(engine)

    # 将爬取成功的文献更新的数据库
    for pdf in pdf_list:
        file_name = pdf.split('.')[0]
        print(file_name)
        paper = session.query(CrawlerStates).filter(CrawlerStates.uniqueid == file_name).first()
        if paper.state ==False:
            paper.state=True
            session.commit()

    session.close()



while True:
    beforePdfSize = len(os.listdir(FILES_STORE))
    cmdline.execute('scrapy crawl wos_spider'.split())
    pdf_list = os.listdir(FILES_STORE)
    updateToDb()
    if len(pdf_list)<=beforePdfSize:
        print("FINISHED GETTING PDF FILES!")
        break