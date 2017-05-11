import os
import random
from scrapy.conf import settings
from ProxyProvider2 import ProxyProvider


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        provider = ProxyProvider()
        proxyss = provider.pick().url
        # print(proxyss)
        request.meta['proxy'] = settings.get(proxyss)