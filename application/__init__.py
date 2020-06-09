from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=getenv('FLASK_BLOG_URI')
app.config['SECRET_KEY']=getenv('SECRET_KEY')


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from application import routes
