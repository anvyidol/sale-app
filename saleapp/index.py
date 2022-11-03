from flask import render_template, request, redirect
from saleapp import app, dao, admin, login
from flask_login import login_user, logout_user

app.secret_key = 'hihi'


@app.route('/')
def home():
    categories = dao.load_categories()
    products = dao.load_products(cate_id=request.args.get('cate_id'), kw=request.args.get('keyword'))
    return render_template('index.html', categories=categories, products=products)


@login.user_loader
def load_user(user_id):
    return dao.get_user_id(user_id)


@app.route('/login-admin', methods=['post'])
def login_admin():
    username = request.form['username']
    password = request.form['password']
    user = dao.user_auth(username, password)
    if user:
        login_user(user=user)
    return redirect('/admin')


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
