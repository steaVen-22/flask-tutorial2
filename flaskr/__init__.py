from flask import Flask
from flask_sqlalchemy import SQLAlchemy# ココ

app = Flask(__name__)
app.config.from_object('flaskr.config')

db = SQLAlchemy(app)

import flaskr.views
