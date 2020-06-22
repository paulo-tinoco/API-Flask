from datetime import datetime
from time import time
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import relationship, backref
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, SmallInteger, Float, DateTime
from . import db


class ProductOrder(db.Model):

    __tablename__ = 'product_order'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    ticket_id = Column(Integer, ForeignKey('orders.id'), nullable=False, unique=False)
    product_id = Column(Integer, ForeignKey('products.id', ondelete="cascade"), nullable=False, unique=False)
    quantity = Column(Integer, nullable=False, unique=False)
    created_at = Column(DateTime, nullable=False, unique=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, unique=False, default=datetime.now, onupdate=datetime.now)
    order = relationship("Orders", cascade="all,delete", backref="order")

    def __repr__(self):
        return f'< ProductOrder {self.product_id} >'
    
    @property
    def serialize(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
        