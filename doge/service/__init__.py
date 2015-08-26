# coding: utf-8
# email: khahux@gmail.com


class Service(object):
    @classmethod
    def instance(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        pass
