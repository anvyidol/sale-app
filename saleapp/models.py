from sqlalchemy.orm import relationship, backref
from saleapp import db, app
from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey, Boolean, Enum, DateTime
from enum import Enum as UserEnum
from flask_login import UserMixin
from datetime import datetime
import hashlib


class UserRole(UserEnum):
    USER = 1
    ADMIN = 2


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class User(BaseModel, UserMixin):
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(Text)
    avatar = Column(Text)
    user_role = Column(Enum(UserRole), default=UserRole.USER)


class Category(BaseModel):
    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


prod_tag = db.Table('prod_tag',
                    Column('product_id', Integer,
                           ForeignKey('product.id'), nullable=False, primary_key=True),
                    Column('tag', Integer,
                           ForeignKey('tag.id'), nullable=False, primary_key=True))


class Product(BaseModel):
    name = Column(String(50), nullable=False)
    description = Column(Text)
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    tags = relationship('Tag', secondary='prod_tag', lazy='subquery',
                        backref=backref('products', lazy=True))
    receipt_details = relationship('ReceiptDetails', backref='product', lazy=True)

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = Column(String(50), nullable=False, unique=True)

    def __str__(self):
        return self.name


class Receipt(BaseModel):
    created_date = Column(DateTime, default=datetime.now())
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    details = relationship('ReceiptDetails', backref='receipt', lazy=True)


class ReceiptDetails(BaseModel):
    quantity = Column(Integer, default=0)
    price = Column(Float, default=0)
    receipt_id = Column(Integer, ForeignKey(Receipt.id), nullable=False)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        # password = str(hashlib.md5('123456'.encode('utf-8')).hexdigest())
        #
        # u = User(name='Admin', username='admin', password=password, avatar='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg', user_role=UserRole.USER)
        # db.session.add(u)
        # db.session.commit()

        # c1 = Category(name="Điện thoại")
        # c2 = Category(name="Máy tính bảng")
        # c3 = Category(name="Phụ kiện")
        #
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()

        # p1 = Product(name='Galaxy S22 Pro', description='Samsung, 128GB', price=25000000,
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
        #              category_id=1)
        # p2 = Product(name='Galaxy Fold 4', description='Samsung, 128GB', price=38000000,
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg',
        #              category_id=1)
        # p3 = Product(name='Apple Watch S5', description='Apple, 32GB', price=18000000,
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
        #              category_id=3)
        # p4 = Product(name='Galaxy Tab S8', description='Samsung, 128GB', price=22000000,
        #              image='https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729569/fi9v6vdljyfmiltegh7k.jpg',
        #              category_id=2)
        # db.session.add_all([p1, p2, p3, p4])
        # db.session.commit()

        db.create_all()
        pass
