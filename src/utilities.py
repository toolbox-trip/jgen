from typing import Tuple
from json import dumps
import gen


def _key(access, type, date) -> str:
    return '{0} {1} {2}'.format(access, type, date)

def public_jwk_key(date) -> str:
    return _key('public', 'jwk', date)


def private_jwk_key(date) -> str:
    return _key('private', 'jwk', date)


def public_pem_key(date) -> str:
    return _key('public', 'pem', date)


def private_pem_key(date) -> str:
    return _key('private', 'pem', date)


def set_new_keys(date, cache) -> Tuple[dict, dict, str, str]:
    (public_jwk, private_jwk, public_pem, private_pem) = gen.new_jwk_pair()
    cache.set_value(public_jwk_key(date), dumps(public_jwk))
    cache.set_value(private_jwk_key(date), dumps(private_jwk))
    cache.set_value(public_pem_key(date), public_pem)
    cache.set_value(private_pem_key(date), private_pem)
    return (public_jwk, private_jwk, public_pem, private_pem)
