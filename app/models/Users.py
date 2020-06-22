from sqlalchemy.inspection import inspect
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, SmallInteger
from . import db


class Users(db.Model):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(45), nullable=False, unique=False)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(130), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False, unique=False)
    status = Column(SmallInteger, nullable=False, unique=False, default=1)

    def __repr__(self):
        return f'< User {self.email}>'
    
    @property
    def serialize(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
