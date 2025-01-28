from django.urls import path

from accounts import views

urlpatterns = [
    path("login/", views.login_to_personal_account, name="login"),
    path("registration/", views.registration, name="registration"),
    path("information/", views.information, name="information"),
    path("metering_devices/", views.metering_devices, name="metering_devices"),
    path("contact/", views.contact, name="contact"),
    path(
        "accrual_and_payment_history/",
        views.accrual_and_payment_history,
        name="accrual_and_payment_history",
    ),
    path("message/", views.message, name="message"),
    path("payment/", views.payment, name="payment"),
    path("receipts/", views.receipts, name="receipts"),
    path("notification/", views.notification, name="notification"),
    path(
        "consumer_personal_accounts/",
        views.consumer_personal_accounts,
        name="consumer_personal_accounts",
    ),
    path("current_period/", views.current_period, name="current_period"),
]
