from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RecentPurchaseSerializer
from .services import RecentPurchasesService


@api_view()
def recent_purchases_view(request, pk):
    username = str(pk)
    service=RecentPurchasesService()
    recent_purchases = service.get_recent_purchases(username)
    serializer = RecentPurchaseSerializer(recent_purchases, many=True)
    return Response(serializer.data)
