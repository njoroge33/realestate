from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^api/users/', views.UserList.as_view(), name='users'),
]