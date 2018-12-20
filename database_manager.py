from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import logging

DB_CONNECT_STRING = 'mysql+mysqlconnector://oeste:huang123@localhost:3306/snkrs'
sqlalchemy_engine = create_engine(DB_CONNECT_STRING)


class MySqlManager:
    def __init__(self):
        self._sessions = sessionmaker(bind=sqlalchemy_engine)

    @staticmethod
    def create_all_table_not_exists(self):
        Base.metadata.create_all(sqlalchemy_engine)

    @property
    def _sessions(self):
        return self._sessions

    def get_session(self):
        return self._sessions()

    @contextmanager
    def short_session(self):
        short_session = self.get_session()
        logging.debug("发起短会话")
        yield short_session
        short_session.commit()
        logging.debug("提交结果")
        short_session.close()
        logging.debug("会话结束")

class RedisManager:
    def __init__(self):
        pass