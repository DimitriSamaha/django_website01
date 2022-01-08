from django.urls import path
from . import views


app_name = "home"

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login_view, name="login"),
    path('register', views.register, name="register"),
    path("logout", views.logout_view, name="logout")
]
