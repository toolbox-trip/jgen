from flask import Flask
from json import dumps
import gen
import base64


app = Flask('jgen')


@app.route('/key')
def generate_key():
    (public_jwk, private_jwk, public_pem, private_pem) = gen.new_jwk_pair()
    data = {
        'public_jwk': public_jwk,
        'private_jwk': private_jwk,
        'public_pem': str(base64.b64encode(public_pem), "utf-8"),
        'private_pem': str(base64.b64encode(private_pem), "utf-8")
    }
    json_str = dumps(data)
    return json_str
