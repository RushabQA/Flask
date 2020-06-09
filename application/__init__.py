from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)




from application import routes
