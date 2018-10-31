from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'civics'
urlpatterns = [
    path('', views.index, name='index'),
    path('log_in/', views.login_page, name='log_in'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('register_user/', views.register_user, name='register_user'),
    path('my_login/', views.my_login, name='my_login'),
    path('detail/<state>/<house>', views.get_senator, name='get_senator'),
    path('detail/', views.get_senator, name='get_senator'),
    path('statement/', views.get_statement, name='get_statement'),
    path('candidate/', views.get_candidate, name='get_candidate'),
]
