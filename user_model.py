from sqlalchemy import Column, String, Integer, Enum
from models import Base


class User(Base):
    __tablename__ = "User"
    UserId = Column('id', Integer, primary_key=True, autoincrement=True)
    Username = Column('username', String(20), nullable=False, unique=True, index=True)
    Password = Column('password', String(20), nullable=False)
    Mail = Column('mail', String(15), nullable=False)
    Region = Column('region', Enum('cn','us'), nullable=False)

    def __repr__(self):
        return "UserId:{},Username:{},Password:{},Mail:{}".format(self.UserId,self.Username,self.Username,self.Password)