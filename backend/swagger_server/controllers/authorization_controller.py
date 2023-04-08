from typing import List
import jwt
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
secretkey = '101_Switching_Protocols'

def check_api_key(api_key, required_scopes):
    return {'test_key': 'test_value'}

def check_user_auth(token):
    dict=jwt.decode(token, secretkey, algorithms=['HS256'])
    return dict

def validate_scope_user_auth(required_scopes, token_scopes):
    return set(required_scopes).issubset(set(token_scopes))


