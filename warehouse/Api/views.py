from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import  RecentPurchaseSerializer
from .models import RecentPurchase
from .services import RecentPurchases
from rest_framework.exceptions import NotFound



@api_view()
def recent_purchases_view(request,pk):
    recent_purchases = []
    
    username=str(pk)
    print(username)
    recent_purchases=RecentPurchases(username).__dict__['recent_purchases']
    if len(recent_purchases)==0:
        raise NotFound('User with username of ' + username + ' was not found!')
    serializer = RecentPurchaseSerializer(recent_purchases,many=True)
    return Response(serializer.data)
   
        
