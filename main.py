# coding=utf-8

from app import doge
from settings import settings

if __name__ == '__main__':
    app = doge()
    app.run(host=settings['host'], port=settings['port'], debug=settings['debug'])
