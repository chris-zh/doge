# coding: utf-8
# email: khahux@gmail.com

from flask_wtf import Form

from doge.service import Service


class BaseForm(Form):
    def __init__(self, *args, **kwargs):
        self.service = Service.instance()
        super(BaseForm, self).__init__(*args, **kwargs)
