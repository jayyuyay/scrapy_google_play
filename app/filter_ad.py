# -*-coding:utf-8-*-
# auth:libai
#
# date:20160119
#
# desc:filter ad from solo_launcher and mongoDB

import requests
import json
import pymongo
import settings


class MongoHandler(object):
    def __init__(self):
        conn = pymongo.Connection(
            settings.MONGODB_HOST,
            settings.MONGODB_PORT
        )
        db_all = conn[settings.MONGODB_DB]
        self.c_all = db_all[settings.MONGODB_COLLECTION]

    def filter_ads(self):
	# self.c_all.remove()
        app = self.c_all.find()
        print app
        urls = []
        url = 'https://play.google.com/store/apps/details?id='
        if app:
            for item in app:
                print item
                print type(item)

                pkg = item.get('pkg')
                pkg_url = url + pkg + '&hl=en'
                urls.append(pkg_url)
        return urls


def get_filter_ads_list():
    # ad_url = 'http://native.solo-launcher.com/api/v1/native_ads?site_id=10265'
    # page = requests.get(ad_url)
    # o = json.loads(page.content)
    # ads = o['ads']
    # ad_l = []
    # url = 'https://play.google.com/store/apps/details?id='
    # for ad in ads:
    #     pkg = ad['packageName']
    #     if pkg:
    #         pkg_url = url + pkg
    #       ad_l.append(pkg_url)
    # ad_solo = list(set(ad_l))
    m = MongoHandler()
    ad_mongo = m.filter_ads()
    # ads = list(set(ad_solo).difference(set(ad_mongo)))
    return ad_mongo

if __name__ == '__main__':
    m = MongoHandler()
    m.filter_ads()
