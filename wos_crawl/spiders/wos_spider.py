import requests
import scrapy
from scrapy import Request
from ..items import WosCrawlItem
from ..model import get_engine, get_session
from ..model.models import CrawlerStates
from ..settings import PROXY_URL
from ..utils.Channel import Channel
from ..settings import DB_PATH
import re

class WosSpiderSpider(scrapy.Spider):
    """
    文献下载爬虫
    """
    name = 'wos_spider'
    def start_requests(self):
        """
        1、拿到代理IP
        2、发起请求
        """
        self.engine = get_engine(DB_PATH)
        self.session = get_session(engine=self.engine)
        # 获取scihub资源链接
        paper_list = self.session.query(CrawlerStates).filter(CrawlerStates.state == False).all()
        for paper in paper_list:
            if paper.doi is None:
                continue
            # proxy = requests.get(PROXY_URL).json().get("proxy")
            detail_url = Channel.getRandChannel() + paper.doi
            # yield Request(url=detail_url,dont_filter=True,
            #                   meta={'proxy': "http://{}".format(proxy), 'unique_id':paper.uniqueid}, callback=self.parse)
            yield Request(url=detail_url, dont_filter=True,
                          meta={ 'unique_id': paper.uniqueid}, callback=self.parse)
            pass

    def parse(self, response):
        """
        解析目标url，将信息写入item字典，传给pipline
        :param response:
        :return:
        """
        detail_url_list = response.xpath('//*[@id="buttons"]/ul/li[2]/a/@onclick')
        if len(detail_url_list) > 0:
            target = detail_url_list.extract_first()
            find_url = re.compile(r"href='(.*?)'")
            target_url = re.findall(find_url, target)[0]
            if target_url[0] != 'h':
                target_url = 'https:' + target_url
            if "\\" in target_url:
                target_url = target_url.replace('\\', '')
            if 'cyber' in target_url:
                return
            # 更新web_url
            # self.session.query(CrawlerStates).filter(CrawlerStates.uniqueid==response.meta['unique_id']).update({'state':True})
            # self.session.commit()

            item = WosCrawlItem()
            item['file_urls'] = []
            item['file_urls'].append(target_url)
            item['name']=response.meta['unique_id']
            yield item
        detail_url_list = response.xpath('//div[@id="buttons"]/button/@onclick')
        if len(detail_url_list) > 0:
            target = detail_url_list.extract_first()
            find_url = re.compile(r"href='(.*?)'")
            target_url = re.findall(find_url, target)[0]
            if target_url[0] != 'h':
                target_url = 'https:' + target_url
            if "\\" in target_url:
                target_url = target_url.replace('\\', '')
            if 'cyber' in target_url:
                return
            # 更新web_url
            # self.session.query(CrawlerStates).filter(CrawlerStates.uniqueid==response.meta['unique_id']).update({'state':True})
            # self.session.commit()

            item = WosCrawlItem()
            item['file_urls'] = []
            item['file_urls'].append(target_url)
            item['name']=response.meta['unique_id']
            yield item
        detail_url_list = response.xpath('//button/@onclick')
        if len(detail_url_list) > 0:
            target = detail_url_list.extract_first()
            find_url = re.compile(r"href='(.*?)'")
            target_url = re.findall(find_url, target)[0]
            if target_url[0] != 'h':
                target_url = 'https:' + target_url
            if "\\" in target_url:
                target_url = target_url.replace('\\', '')
            if 'cyber' in target_url:
                return
            # 更新web_url
            # self.session.query(CrawlerStates).filter(CrawlerStates.uniqueid==response.meta['unique_id']).update({'state':True})
            # self.session.commit()

            item = WosCrawlItem()
            item['file_urls'] = []
            item['file_urls'].append(target_url)
            item['name'] = response.meta['unique_id']
            yield item

        pass
