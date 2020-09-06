from .models import RecentPurchase
from .requestToServer import SendRequest


class RecentPurchasesService():

    recent_purchases = []
    username_of_user = str

    @classmethod
    def get_all_purchases_by_user(cls, username):
        list_recent_purchases = []
        list_recent_purchases = SendRequest.send_request_user_purcheses(
            username)

        for x in list_recent_purchases:
            productId = x['productId']
            cls.add_RecentPurchase_to_list(cls.get_RecentPurchase(productId))
        cls.sort_purchases_by_most_buyers()
        return cls.recent_purchases

    @classmethod
    def sort_purchases_by_most_buyers(cls):
        cls.recent_purchases.sort(key=lambda x: len(x.recent), reverse=True)

    @classmethod
    def remove_username_from_other_buyers(cls, username, list_of_other_buyers):
        data = []
        for buyer in list_of_other_buyers:
            if buyer['username'] != cls.username_of_user:
                data.append(buyer['username'])
        return data

    @classmethod
    def get_RecentPurchase(cls, productId):
        product_details = SendRequest.send_request_product_details(productId)
        buyers_of_product = SendRequest.send_request_buyer_of_product(
            productId)
        list_of_other_buyers = cls.remove_username_from_other_buyers(
            cls.username_of_user, buyers_of_product)
        recent_purchase = cls.create_RecentPurchase(
            product_details, list_of_other_buyers)
        return recent_purchase

    @classmethod
    def create_RecentPurchase(cls, product_details, list_of_other_buyers):
        recent_purchase = RecentPurchase(
            id=product_details['id'],
            face=product_details['face'],
            price=product_details['price'],
            size=product_details['size'],
            recent=list_of_other_buyers)
        return recent_purchase

    @classmethod
    def add_RecentPurchase_to_list(cls, recent_purchase: RecentPurchase):
        cls.recent_purchases.append(recent_purchase)

    @classmethod
    def get_recent_purchases(cls, username):
        cls.recent_purchases.clear()
        cls.username_of_user = username
        data = cls.get_all_purchases_by_user(username)
        return data
