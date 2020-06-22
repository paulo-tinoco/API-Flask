from sqlalchemy.inspection import inspect
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, SmallInteger
from . import db


class Roles(db.Model):

    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(45), nullable=False, unique=False)
    status = Column(SmallInteger, nullable=False, unique=False, default=1)

    def __repr__(self):
        return f'< Role {self.name} >'
    
    @property
    def serialize(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
        