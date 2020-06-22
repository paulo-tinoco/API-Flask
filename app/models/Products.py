from sqlalchemy.inspection import inspect
from sqlalchemy.orm import relationship, backref
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, SmallInteger, Float
from . import db


class Products(db.Model):

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(45), nullable=False, unique=False)
    price = Column(Float, nullable=False, unique=False)
    quantity = Column(Integer, nullable=False, unique=False)
    categories = relationship('Categories', backref=backref('category', lazy='joined'), lazy='dynamic')
    status = Column(SmallInteger, nullable=False, unique=False, default=1)

    def __repr__(self):
        return f'< Product {self.name} >'
    
    @property
    def serialize(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
        