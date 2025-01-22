from django.urls import path

from informations import views

urlpatterns = [
    path("", views.information, name="information"),
]
