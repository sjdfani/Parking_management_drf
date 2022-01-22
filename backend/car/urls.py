from django.urls import path, include
from rest_framework import routers
from .views import CarManagement

app_name = 'car'

router = routers.SimpleRouter()
router.register('', CarManagement, basename='Car_view')

urlpatterns = [
    path('', include(router.urls)),
]
