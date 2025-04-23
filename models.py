from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'
    reason = Column(String, primary_key=True)
    source = Column(String(50), unique=True)
    feeling = Column(String(120), unique=True)

    def __init__(self, reason=None, source=None, feeling=None):
        self.reason = reason
        self.source = source
        self.feeling = feeling

    def __repr__(self):
        return f'<User {self.reason!r}>'