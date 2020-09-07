from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RecentPurchaseSerializer,UsersSerializer
from .services import RecentPurchasesService,UsersService




@api_view()
def recent_purchases_view(request, pk):
    username = str(pk)
    service=RecentPurchasesService()
    serializer = RecentPurchaseSerializer(service.get_recent_purchases(username), many=True)
    return Response(serializer.data)

@api_view()
def users_view(request):
    service=UsersService()
    serializer = UsersSerializer(service.get_users(), many=True)
    return Response(serializer.data)
