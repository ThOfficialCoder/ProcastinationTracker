from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'
    reason = Column(String, primary_key=True)
    source = Column(String(50))
    feeling = Column(String(120))

    def __init__(self, reason=None, source=None, feeling=None):
        self.reason = reason
        self.source = source
        self.feeling = feeling

    def __repr__(self):
        return f'<User {self.reason!r}>'
    
class Task(Base):
    __tablename__ = 'tasks'
    task = Column(String, primary_key=True)

    def __init__(self, task=None):
        self.task = task

    def __repr__(self):
        return f'<Task {self.task!r}>'