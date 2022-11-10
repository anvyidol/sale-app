from saleapp import db
from saleapp.models import Category, Product, User
import hashlib


def load_categories():
    return Category.query.all()


def get_product_by_id(product_id):
    return Product.query.get(product_id)


def load_products(cate_id=None, kw=None):
    query = Product.query.filter(Product.active)
    if cate_id:
        query = query.filter(Product.category_id.__eq__(cate_id))
    if kw:
        query = query.filter(Product.name.contains(kw))
    return query.all()


def user_auth(username, password):
    password = hashlib.md5(password.encode('utf-8')).hexdigest()
    user = User.query.filter(User.username.__eq__(username), User.password.__eq__(password)).first()
    return user


def get_user_id(user_id):
    return User.query.get(user_id)


def register(name, username, password, avatar):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
    u = User(name=name, username=username, password=password, avatar=avatar)
    db.session.add(u)
    db.session.commit()
