from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def getData():
    # 连接数据库
    connect = create_engine("mysql+pymysql://root:rootroot@localhost:3306/douban_finished",
                            encoding="utf-8",
                            echo=True)
    Base = declarative_base()

    # 构造表的结构
    class Finished(Base):
        __tablename__ = "finished"
        id = Column(Integer,primary_key=True,nullable=False)
        category = Column(String(255))
        name = Column(String(255),nullable=False)

    # 如果User表不存在的话，就创建改表
    Base.metadata.create_all(connect)

    DBsession = sessionmaker(bind=connect)
    session = DBsession()

    finishedLs = session.query(Finished).all()

    fini_dict = {}
    for i in finishedLs:
        fini_dict[i.name] = i.category

    #print(fini_dict.keys())
    return fini_dict

# {'解忧杂货店': 'book', '2012': 'movie', '你好，旧时光': 'movie', '十面埋伏': 'movie', '小丑': 'movie', '寻梦环游记': 'movie', '心灵捕手': 'movie', '环太平洋': 'movie', '疯狂动物城': 'movie', '7 years': 'music', '倒数': 'music', '句号': 'music'}
# fini_dict.keys() 得到key的列表

getData()