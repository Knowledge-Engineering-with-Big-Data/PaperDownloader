import os

from model.models import CrawlerStates
from settings import FILES_STORE,DB_PATH
from model import get_engine,get_session

if __name__ == '__main__':

    pdf_list = os.listdir(FILES_STORE)
    engine = get_engine(DB_PATH)
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