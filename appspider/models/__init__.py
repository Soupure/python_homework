from datetime import datetime

import sqlalchemy
from sqlalchemy import Column, Integer, DateTime, TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('sqlite:///app.db', echo=False)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class App(Base):
    __tablename__ = 'app'
    id = Column(Integer, primary_key=True)
    title = Column(TEXT, nullable=False)
    url = Column(TEXT, nullable=False, unique=True, index=True)
    icon = Column(TEXT, nullable=False)
    desc = Column(TEXT)
    source = Column(TEXT, nullable=False)
    status = Column(Integer, default=0)
    createtime = Column(DateTime, nullable=False, default=datetime.utcnow)


Base.metadata.drop_all(engine) #备注后抓取多页
Base.metadata.create_all(engine)
