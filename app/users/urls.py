from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('users/', views.get_all_users, name='get_all_users'),
]
