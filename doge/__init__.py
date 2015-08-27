# coding: utf-8
# email: khahux@gmail.com

from flask import Flask
from config import configs


app = Flask(__name__)
app.config.update(**configs)

from doge.views import home
app.register_blueprint(home.mod)
