from datetime import date
from typing import Tuple
from authlib.jose import jwk
from Cryptodome.PublicKey import RSA


def new_key_pair():
    key = RSA.generate(2048)
    return (key.publickey().export_key(), key.export_key())


def new_jwk_pair() -> Tuple[dict, dict, str, str]:
    # new RSA key pair
    (public_rsa_bytes, private_rsa_bytes) = new_key_pair()
    # public jwk dict
    public_jwk = jwk.dumps(public_rsa_bytes, kty='RSA', use='sig', kid='{0}'.format(date.today().strftime('%Y-%m-%d')))
    # private jwk dict
    private_jwk = jwk.dumps(private_rsa_bytes, kty='RSA', kid='{0}'.format(date.today().strftime('%Y-%m-%d')))
    return (public_jwk, private_jwk, public_rsa_bytes, private_rsa_bytes)
