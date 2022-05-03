from . import views
from django.urls import path

app_name = 'speed_test'
urlpatterns = [
    path('', views.index, name='index'),
    path('type_test', views.type_test, name='type_test'),
    path('equ_solve', views.equ_solve, name='equ_solve')
]
