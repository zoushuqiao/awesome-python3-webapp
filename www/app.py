
# -*- coding: utf-8 -*-

'''
async web application.
'''

from aiohttp import web
import time
import json
import os
import asyncio
import logging
logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body='Awesome')


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
