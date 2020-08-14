from django.db import models

class RecentPurchase(object):
    def __init__(self, id, face, price, size, recent):
        self.id = id
        self.face = face
        self.price = price
        self.size = size
        self.recent = recent

   
