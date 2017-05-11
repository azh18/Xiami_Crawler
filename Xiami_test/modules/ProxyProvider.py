# -*- coding: utf-8 -*-

import logging
import random
import threading
import requests
import ujson

from modules.Proxy import Proxy

logger = logging.getLogger()


class ProxyProvider:
    def __init__(self, min_proxies=200):
        self._bad_proxies = {}
        self._minProxies = min_proxies
        self.lock = threading.RLock()
        self._proxies_path = './proxies.txt'
        self._proxies = []
        self.get_list()

    @property
    def proxies(self):
        return self._proxies

    def get_list(self):
        logger.debug("Getting proxy list")
        try:
            r = requests.get("https://jsonblob.com/api/jsonBlob/31bf2dc8-00e6-11e7-a0ba-e39b7fdbe78b", timeout=10)
            proxies = ujson.decode(r.text)
            logger.debug("Got %s proxies", len(proxies))
            self._proxies = list(map(lambda p: Proxy(p), proxies))
            self.write_proxies(r.text)
        except requests.RequestException:
            print('Proxy url request failed, read local proxy list!')
            self.read_local_proxies()

    def write_proxies(self, content):
        with open(self._proxies_path, 'w') as f:
            f.write(content)

    def read_local_proxies(self):
        with open(self._proxies_path, 'r') as f:
            proxies_text = f.readlines()
            proxies = ujson.loads(proxies_text[0])
            logger.debug("Got %s proxies", len(proxies))
            self._proxies = list(map(lambda p: Proxy(p), proxies))

    def pick(self):
        with self.lock:
            self._proxies.sort(key = lambda p: p.score, reverse=True)
            proxy_len = len(self._proxies)
            max_range = 50 if proxy_len > 50 else proxy_len
            proxy = self._proxies[random.randrange(1, max_range)]
            proxy.used()

            return proxy

    def count(self):
        with self.lock:
            return len(self._proxies)

if __name__ == "__main__":
    provider = ProxyProvider()
    print(provider.pick().url)
