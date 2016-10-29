# -*- coding:utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.autoreload
from tornado.options import define, options
import settings
import pymongo
import json
from tornado.web import asynchronous
import tornado.gen
from spider import get_from_gp
define("port", default=9999, help="run on the given port", type=int)


# @tornado.gen.coroutine
# def render_response(app):
#     value = dict(
#         status='ok',
#         lib_in='yes',
#         ads=app
#     )
#     raise tornado.gen.Return(json.dumps(value))

# @tornado.gen.coroutine
# def get_from_gp():
#     pass


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/api', AppsHandler),
        ]
        super(Application, self).__init__(handlers)
        #conn = pymongo.Connection(
        #    settings.MONGODB_HOST,
        #    settings.MONGODB_PORT
        #)
        #db = conn[settings.MONGODB_DB]
        #self.co = db[settings.MONGODB_COLLECTION]


class AppsHandler(tornado.web.RequestHandler):
    # @property
    # def co(self):
    #     return self.application.co

    @asynchronous
    @tornado.gen.coroutine
    def get(self):
        pkg = self.get_argument('pkg')
        #app = self.co.find_one({'pkg': pkg})
        #if app:
        #    app.pop('_id')
        #    values = yield render_response(app)
        #    self.write(values)
        #else:
        values = yield get_from_gp(pkg)
        if values['status'] == 'no data':
            self.write(values)
        else:
            self.write(values)
            # values.pop('_id',True)
            # values.pop('status')
            # values.pop('lib_in')
            # self.co.save(values['ads'])

if __name__ == "__main__":
    options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    print "Application starts on port: ", options.port
    tornado.ioloop.IOLoop.instance().start()
