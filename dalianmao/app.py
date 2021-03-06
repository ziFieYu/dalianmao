import asyncio

try:
    import uvloop
except:
    pass
else:
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

from dalianmao.options import Options
from dalianmao.router import Router
from dalianmao.engine import Engine


class DaLianMao:

    def __init__(self, options, loop=None):
        if not loop:
            loop = asyncio.get_event_loop()
        self.loop = loop
        self.router = Router()
        self.engine = Engine(loop, options, self.router)
        self.download = self.engine.client.download

    def route(self, url, method='GET', params=None, data=None, json=False, extract_urls=None):

        def wrapper(handler):
            self.router.add(handler, url, method, params, data, json, extract_urls)

        return wrapper

    def add_route(self, handler, url, method='GET', params=None, data=None, json=False, extract_urls = None):
        self.route(url, method, params, data, dynamic, json)(handler)

    def remove_route(self, url):
        self.router.remove(url)

    def add_proxy_handler(self, proxy_handler):
        self.engine.client.proxy_handler = proxy_handler

    def crawl(self):
        self.engine.run()
