from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'civics'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('detail/<state>/<house>', views.get_senator, name='get_senator'),
    path('detail/', views.get_senator, name='get_senator'),
    path('statement/', views.get_statement, name='get_statement'),
    path('candidate/', views.get_candidate, name='get_candidate'),
]
