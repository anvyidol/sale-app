from flask import render_template, request, redirect
from saleapp import app, dao, login
from flask_login import login_user, logout_user
import cloudinary.uploader

app.secret_key = 'hihi'


@app.route('/')
def home():
    products = dao.load_products(cate_id=request.args.get('cate_id'), kw=request.args.get('keyword'))
    return render_template('index.html', products=products)


@app.route('/product/<int:product_id>')
def product_detail(product_id):
    p = dao.get_product_by_id   (product_id)
    return render_template('details.html', product=p)


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


@app.route('/register', methods=['get', 'post'])
def register_user():
    err_msg = ''
    if request.method == 'POST':
        password = request.form['password']
        confirm = request.form['confirm']

        if password.__eq__(confirm):
            # upload avatar
            avatar = ''
            if request.files:
                res = cloudinary.uploader.upload(request.files['avatar'])
                avatar = res['secure_url']

            # luu user
            try:
                dao.register(name=request.form['name'],
                             username=request.form['username'],
                             password=request.form['password'],
                             avatar=avatar)

                return redirect('/login')
            except:
                err_msg = 'Có lỗi xảy ra! Vui lòng quay lại sau!'
        else:
            err_msg = 'Mật khẩu KHÔNG khớp!'

    return render_template('register.html', err_msg=err_msg)


@app.route('/login', methods=['get', 'post'])
def login_my_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = dao.user_auth(username=username, password=password)
        if user:
            login_user(user)
            return redirect('/')

    return render_template('login.html')


@app.route('/logout')
def logout_my_user():
    logout_user()
    return redirect('/login')


@app.context_processor
def common_attr():
    categories = dao.load_categories()
    return {
        'categories': categories
    }


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
