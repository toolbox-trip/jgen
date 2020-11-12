from flask import Flask
from json import dumps
from cache import Cache
from utilities import private_jwk_key, private_pem_key, public_jwk_key, public_pem_key, set_new_keys


app = Flask('jgen')
cache = Cache()


@app.route('/jwk/<date>')
def get_jwk(date):
    cached_value = cache.get_value(public_jwk_key(date))
    if cached_value is None:
        (public_jwk, private_jwk, public_pem, private_pem) = set_new_keys(date, cache)
        json_str = dumps(public_jwk)
        return json_str
    else:
        return cached_value


@app.route('/private/jwk/<date>')
def get_private_jwk(date):
    cached_value = cache.get_value(private_jwk_key(date))
    if cached_value is None:
        (public_jwk, private_jwk, public_pem, private_pem) = set_new_keys(date, cache)
        json_str = dumps(private_jwk)
        return json_str
    else:
        return cached_value


@app.route('/public/pem/<date>')
def get_public_pem(date):
    cached_value = cache.get_value(public_pem_key(date))
    if cached_value is None:
        (public_jwk, private_jwk, public_pem, private_pem) = set_new_keys(date, cache)
        return public_pem
    else:
        return cached_value


@app.route('/private/pem/<date>')
def get_private_pem(date):
    cached_value = cache.get_value(private_pem_key(date))
    if cached_value is None:
        (public_jwk, private_jwk, public_pem, private_pem) = set_new_keys(date, cache)
        return private_pem
    else:
        return cached_value
