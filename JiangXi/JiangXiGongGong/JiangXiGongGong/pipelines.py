# -*- coding: utf-8 -*-
import pymongo
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JiangxigonggongPipeline(object):
    def __init__(self):
        self.Mongo_Client = pymongo.MongoClient()
        self.Mongo_DB = self.Mongo_Client['HeBei']
        self.Mongo_TB = self.Mongo_DB['invitation']


    def process_item(self,item,spider):
        if spider.class_type == '1':
            dict_data = dict(item)
            self.Mongo_TB.insert(dict_data)
            return item

        if spider.class_type == '2':
            self.Mongo_TB = self.Mongo_DB['winbid']
            dict_data = dict(item)
            self.Mongo_TB.insert(dict_data)
            return item
