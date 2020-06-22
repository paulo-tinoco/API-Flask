from datetime import datetime
from time import time
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import relationship, backref
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, SmallInteger, Float, DateTime
from . import db


class Orders(db.Model):

    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, unique=False)
    created_at = Column(DateTime, nullable=False, unique=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, unique=False, default=datetime.now, onupdate=datetime.now)
    status = Column(SmallInteger, nullable=False, unique=False, default=1)

    def __repr__(self):
        return f'< Order {self.id} >'
    
    @property
    def serialize(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
        