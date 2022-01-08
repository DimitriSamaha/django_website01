from django.urls import path
from . import views


app_name = 'rockpaperscissors'
urlpatterns = [
    path('', views.index, name='index')
]