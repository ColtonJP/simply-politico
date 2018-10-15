
from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'civics'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('register_user/', views.register_user, name='register_user'),
    path('mylogin/', views.mylogin, name='mylogin'),
    path('getsenator/', views.getsenator, name='getsenator'),

]