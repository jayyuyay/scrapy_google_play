# -*- coding: utf-8 -*-

import time
import scrapy
from app.items import GoogleItem
from app.filter_ad import get_filter_ads_list
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class GoogleSpider(scrapy.Spider):
    name = "google"
    allowed_domains = ["play.google.com"]
    start_urls = get_filter_ads_list()

    def parse(self, response):
        item = GoogleItem()
        item['url'] = response.url
        try:
            item['pkg'] = response.url.split('=')[1].split('&')[0]
        except IndexError:
            item['pkg'] = response.url.split('=')[1]
        try:
            item['evaluate'] = response.xpath("//div[@class='score']/text()").extract()[0].strip()
        except IndexError:
            item['evaluate'] = ''
        try:
            item['comment_count'] = response.xpath("//span[@class='reviews-num']/text()").extract()[0].strip().replace(',','')
        except IndexError:
            item['comment_count'] = ''
        try:
            item['category'] = response.xpath("//span[@itemprop='genre']/text()").extract()
        except IndexError:
            item['category'] = ''
        try:
            item['app_name'] = response.xpath("//div[@class='id-app-title']/text()").extract()[0].strip()
        except IndexError:
            item['app_name'] = ''

        t = response.xpath("//div[@itemprop='datePublished']/text()")
        try:
            item['update_time'] = time.strftime("%Y%m%d", time.strptime(t.extract()[0].strip(), '%B %d, %Y'))
        except IndexError:
            item['update_time'] = ''
        except ValueError:
            try:
                item['update_time'] = time.strftime("%Y%m%d", time.strptime(t.extract()[0].strip(), '%d %B %Y'))
            except ValueError:
                item['update_time'] = time.strftime("%Y%m%d", time.strptime(t.extract()[0].strip(), u'%Y年%m月%d日'))
        try:
            item['install_num'] = response.xpath("//div[@itemprop='numDownloads']/text()").extract()[0].strip().replace(',','').replace(' ','')
        except IndexError:
            item['install_num'] = ''
        try:
            item['app_version'] = response.xpath("//div[@itemprop='softwareVersion']/text()").extract()[0].strip()
        except IndexError:
            item['app_version'] = ''
        try:
            item['android_version_need'] = response.xpath("//div[@itemprop='operatingSystems']/text()").extract()[0].strip()
        except IndexError:
            item['android_version_need'] = ''
        try:
            item['content_rate'] = response.xpath("//div[@itemprop='contentRating']/text()").extract()[0].strip()
        except IndexError:
            item['content_rate'] = ''
        try:
            item['provider'] = response.xpath("//span[@itemprop='name']/text()").extract()[0].strip()
        except IndexError:
            item['provider'] = ''
        try:
            item['app_size'] = response.xpath("//div[@itemprop='fileSize']/text()").extract()[0].strip()
        except IndexError:
            item['app_size'] = ''
        try:
            item['app_msg'] = response.xpath("//div[@class='inapp-msg']/text()").extract()[0].strip()
        except IndexError:
            item['app_msg'] = ''
        try:
            item['description'] = ''.join(response.xpath("//div[@jsname='C4s9Ed']/text()").extract()) +\
                                  ''.join(response.xpath('//div[@jsname="C4s9Ed"]//p/text()').extract())
        except IndexError:
            item['description'] = ''
        yield item
