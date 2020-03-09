from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def addFini(cate,name):
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

    # 为表添加数据
    new_fini = Finished(category=cate,name=name)

    DBsession = sessionmaker(bind=connect)
    session = DBsession()

    #事务操作
    session.add(new_fini)
    session.commit()
    session.close()