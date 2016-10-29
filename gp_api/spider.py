# -*-coding:utf-8-*-

import requests
from lxml import html
import tornado.gen
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


@tornado.gen.coroutine
def get_from_gp(pkg):
    head = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            }
    url = 'https://play.google.com/store/apps/details?id=' + pkg + '&hl=en'
    page = requests.get(url, timeout=5, headers=head, verify=False)
    if page.status_code == 200:
        tree_page = html.fromstring(page.content)
        try:
            evaluate = tree_page.xpath("//div[@class='score']/text()")[0].strip()
        except IndexError:
            evaluate = ''
        try:
            comment_count = tree_page.xpath("//span[@class='reviews-num']/text()")[0].strip().replace(',','')
        except IndexError:
            comment_count = ''
        try:
            category = tree_page.xpath("//span[@itemprop='genre']/text()")
        except IndexError:
            category = ''
        try:
            app_name = tree_page.xpath("//div[@class='id-app-title']/text()")[0].strip()
        except IndexError:
            app_name = ''

        t = tree_page.xpath("//div[@itemprop='datePublished']/text()")
        try:
            update_time = time.strftime("%Y%m%d", time.strptime(t[0].strip(), '%B %d, %Y'))
        except IndexError:
            update_time = ''
        except ValueError:
            try:
                update_time = time.strftime("%Y%m%d", time.strptime(t[0].strip(), '%d %B %Y'))
            except ValueError:
                update_time = time.strftime("%Y%m%d", time.strptime(t[0].strip(), u'%Y年%m月%d日'))
        try:
            install_num = tree_page.xpath("//div[@itemprop='numDownloads']/text()")[0].strip().replace(',','').replace(' ','')
        except IndexError:
            install_num = ''
        try:
            app_version = tree_page.xpath("//div[@itemprop='softwareVersion']/text()")[0].strip()
        except IndexError:
            app_version = ''
        try:
            android_version_need = tree_page.xpath("//div[@itemprop='operatingSystems']/text()")[0].strip()
        except IndexError:
            android_version_need = ''
        try:
            content_rate = tree_page.xpath("//div[@itemprop='contentRating']/text()")[0].strip()
        except IndexError:
            content_rate = ''
        try:
            provider = tree_page.xpath("//span[@itemprop='name']/text()")[0].strip()
        except IndexError:
            provider = ''
        try:
            app_size = tree_page.xpath("//div[@itemprop='fileSize']/text()")[0].strip()
        except IndexError:
            app_size = ''
        try:
            app_msg = tree_page.xpath("//div[@class='inapp-msg']/text()")[0].strip()
        except IndexError:
            app_msg = ''
        # try:
        #     description = ''.join(tree_page.xpath("//div[@jsname='C4s9Ed']/text()")) +\
        #                           ''.join(tree_page.xpath('//div[@jsname="C4s9Ed"]//p/text()'))
        # except IndexError:
        #     description = ''
        value = {
                'status': 'ok',
                'ads':
                    {
                    'url': url,
                    'pkg': pkg,
                    'evaluate': evaluate,
                    'comment_count': comment_count,
                    'category': category,
                    'app_name': app_name,
                    'update_time': update_time,
                    'install_num': install_num,
                    'app_version': app_version,
                    'android_version_need': android_version_need,
                    'content_rate': content_rate,
                    'provider': provider,
                    'app_size': app_size,
                    'app_msg': app_msg,
                    }
                }
        raise tornado.gen.Return(value)
    else:
        value = {'status': 'no data'}
        raise tornado.gen.Return(value)
    
if __name__ == "__main__":
    get_from_gp('com.oovoo')
