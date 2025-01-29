from django.urls import path, include
from .views import *

urlpatterns = [
    path("", land, name="land"),
    path("signup/", authView, name="signup"),
    path("login/", loginu, name="login"),
    path("create-checkout-session/", create_checkout_session, name='create_checkout_session'),
    path("success/", success, name="success"),
    path("cancel/", cancel, name="cancel"),
    path("orders/", orders, name="orders"),
    path("error/", error, name="error"),
    path("dashboard/", home, name="home"),
    path("profile/", profile, name="profile"),
    path('logout/', logout_view, name='logout'),
    path('profile/delete/', delete_account, name='profile_delete'),
    path("profile/update/", update_profile, name="profile_update"),

]