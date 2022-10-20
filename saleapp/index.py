from flask import render_template, request
from saleapp import app, dao
import logging


@app.route('/')
def home():
    categories = dao.load_categories()
    products = dao.load_products(cate_id=request.args.get('cate_id'))
    return render_template('index.html', categories=categories, products=products)


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)

