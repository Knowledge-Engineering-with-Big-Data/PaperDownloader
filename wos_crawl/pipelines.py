# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy import Request
from scrapy.pipelines.files import FilesPipeline
from .model import get_engine, get_session
from .model.models import CrawlerStates
from .settings import DB_PATH

class fileDown(FilesPipeline):

    def item_completed(self, results, item, info):
        uniqueid = item['name']
        # if results[0][0] == True:
        #     engine = get_engine(DB_PATH)
        #     session = get_session(engine)
            # session.query(CrawlerStates).filter(CrawlerStates.uniqueid == uniqueid).update(
            #     {'state': True})
            # session.commit()
        return super().item_completed(results, item, info)

    def get_media_requests(self, item, info):
        # 向FilesPipline提交url地址，进行文件下载
        self.name = item['name']
        for url in item['file_urls']:
            yield Request(url)

    def file_path(self, request, response=None, info=None):
        file_name = self.name + '.pdf'
        return file_name
