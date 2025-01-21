from django.urls import path
from accounts import views

urlpatterns = [
    path("login/", views.login_to_personal_account, name="login"),
    path("registration/", views.registration, name="registration"),
    path("information/", views.information, name="information"),
]
