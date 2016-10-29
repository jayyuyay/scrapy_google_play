# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GoogleItem(scrapy.Item):
    url = scrapy.Field()
    update_time = scrapy.Field()
    app_version = scrapy.Field()
    install_num = scrapy.Field()
    category = scrapy.Field()
    comment_count = scrapy.Field()
    evaluate = scrapy.Field()
    android_version_need = scrapy.Field()
    content_rate = scrapy.Field()
    provider = scrapy.Field()
    app_name = scrapy.Field()
    app_size = scrapy.Field()
    app_msg = scrapy.Field()
    pkg = scrapy.Field()
    description = scrapy.Field()
