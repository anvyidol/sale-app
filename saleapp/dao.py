import json
from saleapp import app


def load_categories():
    with open(f'{app.root_path}/data/categories.json', encoding='utf-8') as f:
        return json.load(f)


def load_products(cate_id=None):
    with open(f'{app.root_path}/data/products.json', encoding='utf-8') as f:
        products = json.load(f)
    if cate_id:
        products = filter(lambda p: p.category_id == cate_id, products)

    return products
