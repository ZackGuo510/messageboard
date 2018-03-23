from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='url_name_home'),
    path('write', views.Write.as_view(), name='write'),
]
