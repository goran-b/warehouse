from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import  recent_purchases_view


router= routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('recent_purchases/<str:pk>', recent_purchases_view, name='recent_purchases_view'),
]