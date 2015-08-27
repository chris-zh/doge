# coding: utf-8
# email: khahux@gmail.com

from doge import app
from config import configs

app.run(host=configs['HOST'], port=configs['PORT'], debug=configs['DEBUG'])
