# coding=utf-8

from flask import Module, render_template


home = Module(__name__)


@home.route('/', methods=['GET'])
def index():
    return render_template('index.html')
