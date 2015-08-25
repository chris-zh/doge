# coding=utf-8

import peewee as models

from settings import db_settings


class Database(models.MySQLDatabase):
    pass


db = Database(**db_settings)


class Model(models.Model):
    class Meta:
        database = db
