from django.urls import path, re_path, include
from . import views
from .views import UserList
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserList)

urlpatterns = [
    re_path(r'^', include(router.urls)),
    # re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]