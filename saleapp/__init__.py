from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager
from flask_babelex import Babel
import cloudinary

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/saleappvjppro?charset=utf8mb4' % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

app.config['CART_KEY'] = 'cart'

db = SQLAlchemy(app=app)

login = LoginManager(app=app)

babel = Babel(app)

cloudinary.config(cloud_name='by1410ou', api_key='949254188268352', api_secret='ZLvdD3BR4qe2ueXvmV7ltAOkkjQ')


@babel.localeselector
def get_locale():
    return "vi"


