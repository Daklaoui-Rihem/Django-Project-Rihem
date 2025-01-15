from django.urls import path, include
from .views import authView,home,loginu

urlpatterns = [
    path("", home, name="home"),
    path("signup/", authView, name="signup"),
    path("login/", loginu, name="login"),
]