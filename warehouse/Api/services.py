import requests
import json
from .models import RecentPurchase
from rest_framework.exceptions import NotFound

recent_purchases = []
username_of_user = str

def throw_error_no_user(username,user_response):
    if len(user_response)==0:
        raise NotFound('User with username of ' + username + ' was not found!')

def get_all_purchases_by_user(username):
    list_recent_purchases = []
    list_recent_purchases = SendRequest.send_request_user_purcheses(username)

    for x in list_recent_purchases:
        productId = x['productId']
        add_RecentPurchase_to_list(get_RecentPurchase(productId))
    sort_purchases_by_most_buyers()
    return recent_purchases


def sort_purchases_by_most_buyers():
    recent_purchases.sort(key=lambda x: len(x.recent), reverse=True)

class SendRequest():

    API_URL = 'http://127.0.0.1:4000/api/'

    @classmethod
    def send_request_user_purcheses(cls, username):
        response = requests.get(
            f"{cls.API_URL}purchases/by_user/{username}?limit=5")
        data = response.json()['purchases']
        throw_error_no_user(username,data)
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


def remove_username_from_other_buyers(username, list_of_other_buyers):
    data = []
    for buyer in list_of_other_buyers:
        if buyer['username'] != username_of_user:
            data.append(buyer['username'])
    return data


def get_RecentPurchase(productId):
    product_details = SendRequest.send_request_product_details(productId)
    buyers_of_product = SendRequest.send_request_buyer_of_product(
        productId)
    list_of_other_buyers = remove_username_from_other_buyers(
        username_of_user, buyers_of_product)
    recent_purchase = create_RecentPurchase(
        product_details, list_of_other_buyers)
    return recent_purchase


def create_RecentPurchase(product_details, list_of_other_buyers):
    recent_purchase = RecentPurchase(
        id=product_details['id'],
        face=product_details['face'],
        price=product_details['price'],
        size=product_details['size'],
        recent=list_of_other_buyers)
    return recent_purchase


def add_RecentPurchase_to_list(recent_purchase: RecentPurchase):
    recent_purchases.append(recent_purchase)


def get_recent_purchases(username):
    recent_purchases.clear()
    username_of_user = username
    data = get_all_purchases_by_user(username)
    return data
