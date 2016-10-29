# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import settings


class MongoDBPipeline(object):
    def __init__(self):
        conn = pymongo.Connection(
            settings.MONGODB_HOST,
            settings.MONGODB_PORT
        )
        db = conn[settings.MONGODB_DB]
        self.c = db[settings.MONGODB_COLLECTION]

    def process_item(self, item, spider):
        self.c.update({'pkg': item['pkg']}, dict(item), upsert=True)
        return item
