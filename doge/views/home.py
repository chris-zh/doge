# coding: utf-8
# email: khahux@gmail.com

from flask import Blueprint, render_template


mod = Blueprint('', __name__, url_prefix='')


@mod.route('/')
def index():
    return render_template('home/home.html')
