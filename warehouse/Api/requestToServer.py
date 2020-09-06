import requests
import json
from .errors import Errors

class SendRequest():

    API_URL = 'http://127.0.0.1:4000/api/'

    @classmethod
    def send_request_user_purcheses(cls, username):
        response = requests.get(
            f"{cls.API_URL}purchases/by_user/{username}?limit=5")
        data = response.json()['purchases']
        Errors.throw_error_no_user(username, data)
        return data

    @classmethod
    def send_request_product_details(cls, productId):
        response = requests.get(
            f"{cls.API_URL}products/{str(productId)}")
        data = response.json()['product']
        return data

    @classmethod
    def send_request_buyer_of_product(cls, productId):
        response = requests.get(
            f"{cls.API_URL}purchases/by_product/{str(productId)}")
        data = response.json()['purchases']
        return data
