# coding:utf-8
__author__ = 'mfserver'

from sqlalchemy import Column, Integer, String, create_engine, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/dbtest?charset=utf8", max_overflow=5)
Base = declarative_base()


class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32))
    password = Column(String(32))

    __table_args__ = (
        UniqueConstraint('username', 'password', name='uix_id_name'),
    )


def init_table():
    '''
    创建表
    :return:
    '''
    Base.metadata.create_all(engine)


def drop_table():
    '''
    删除表
    :return:
    '''
    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    init_table()

