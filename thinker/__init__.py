from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='this-should-be-changed-at-some-point-i-guess'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'

db = SQLAlchemy(app)

from thinker import routes