#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/2/3 20:53
# @Author : ZhangXiaobo
# @Software: PyCharm
from scrapy import cmdline
cmdline.execute('scrapy crawl wos_spider'.split())