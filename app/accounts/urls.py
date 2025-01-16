from django.urls import path
from accounts import views

urlpatterns = [
    path("login/", views.login_to_personal_account),
    path("registration/", views.registration, name="registration"),
    path("", views.login_to_personal_account, name="index"),
]
