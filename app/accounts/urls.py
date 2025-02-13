from django.urls import path

from accounts import views

urlpatterns = [
    path("login/", views.log_in, name="login"),
    # path("registration/", views.registration, name="registration"),
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
    path("receipts/", views.receipts, name="receipts"),
    path("notification/", views.notification, name="notification"),
    path(
        "consumer_personal_accounts/",
        views.consumer_personal_accounts,
        name="consumer_personal_accounts",
    ),
    path("current_period/", views.current_period, name="current_period"),
    path("assessment/", views.assessment, name="assessment"),
    path("paying/", views.paying, name="paying"),
    path("settings_user/", views.settings_user, name="settings_user"),
    path("log_out/", views.log_out, name="log_out"),
    path("payment/", views.payment, name="payment"),
]
