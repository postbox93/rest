from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('emp',EmployeeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
]