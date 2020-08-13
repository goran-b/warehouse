import requests
import json
from .models import RecentPurchase


class RecentPurchases:
    def __init__(self,username,recent_purchases = []):
        self.username= username
        self.recent_purchases = recent_purchases
        
        
        def get_recent_purchases_user(username):
            response_recent_purchases_user=requests.get('http://127.0.0.1:4000/api/purchases/by_user/'+ username+'?limit=5')
            list_recent_purchases= response_recent_purchases_user.json()['purchases']

            for x in list_recent_purchases:
                print(x['productId'])
                productId=x['productId']
                get_data_purchases(productId) 

            recent_purchases.sort(key=lambda x: len(x.recent), reverse=True)
            newlist = sorted(recent_purchases,key=lambda x: len(x.recent), reverse=False)
        
                
        def get_data_purchases(id):
            product_details=get_product_details(id)
            other_buyers_of_product=get_other_buyers_of_product(id)
                     
            recent_purchase = RecentPurchase(
                id=product_details['id'],
                face=product_details['face'], 
                price=product_details['price'], 
                size=product_details['size'],
                recent=other_buyers_of_product)

            recent_purchases.append(recent_purchase)
            

        def get_product_details(id):
            response_product_details=requests.get('http://127.0.0.1:4000/api/products/'+ str(id))         
            product_details = response_product_details.json()['product']
            return product_details


        def get_other_buyers_of_product(id):
            response_other_buyers_of_product=requests.get('http://127.0.0.1:4000/api/purchases/by_product/'+ str(id))         
            other_buyers_of_product = response_other_buyers_of_product.json()['purchases']
            list_of_other_buyers=[]
            for e in other_buyers_of_product:
                if e['username'] != self.username:
                    list_of_other_buyers.append(e['username'])   
            return list_of_other_buyers


        def main(self,username):
            get_recent_purchases_user(username) 
       

        main(self,username)
                

     


   



    