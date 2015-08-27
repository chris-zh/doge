# coding: utf-8
# email: khahux@gmail.com

from pymongo import MongoClient

from config import mongodb_configs


client = MongoClient(host=mongodb_configs['host'], port=mongodb_configs['port'])
db = client[mongodb_configs['doge']]
