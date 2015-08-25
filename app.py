# coding=utf-8

from flask import Flask

from handlers.home import home
from settings import settings


def doge():
    app = Flask(__name__)
    app.secret_key = settings['SECRET_KEY']
    app.register_module(home)

    return app
