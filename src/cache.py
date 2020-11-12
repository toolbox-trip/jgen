from typing import Optional
from pymemcache.client.base import Client
from os import environ

_MEMCACHED_ADDR = 'MEMCACHED_ADDR' #'172.17.0.2'
_MEMCACHED_PORT = 'MEMCACHED_PORT' #'11211'


class DictCache(object):
    def __init__(self) -> None:
        self._d = dict()

    def set_value(self, key, value):
        self._d[key] = value

    def get_value(self, key):
        return self._d.get(key)


class MemcachedCache(object):
    def __init__(self, addr, port) -> None:
        # TODO: read config from env
        self._client = Client('{}:{}'.format(addr, port), encoding='utf8')

    def set_value(self, key: str, value: str):
        self._client.set(key, value)

    def get_value(self, key):
        return self._client.get(key)


class Cache(object):
    def __init__(self) -> None:
        addr = environ[_MEMCACHED_ADDR]
        port = environ[_MEMCACHED_PORT]
        if (addr is None) or (len(addr) == 0) or (port is None) or (len(port) == 0):
            self.inner_cache = DictCache()
        else:
            self.inner_cache = MemcachedCache()

    def set_value(self, key: str, value: str) -> None:
        self.inner_cache.set_value(key, value)

    def get_value(self, key: str) -> Optional[str]:
        return self.inner_cache.get_value(key)
