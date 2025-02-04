import os

from django.shortcuts import redirect, render
from dotenv import load_dotenv

from accounts.models import CustomUsers

_ = load_dotenv()


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        custom_user = CustomUsers.objects.filter(email=email, password=password).first()
        if custom_user:
            return redirect("information")
        else:
            context = {
                "site_title": "Авторизация",
            }

            return render(request, "login.html", context=context)

    context = {
        "site_title": "Авторизация",
    }
    return render(request, "login.html", context=context)


def settings_user(request):
    user = request.user

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")

        if full_name:
            print(user)

    context = {
        "site_title": "Настройки",
        "full_name": "ФИО",
        "email": "email",
    }

    return render(request, "settings_user.html", context=context)


def registration(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")

        if full_name and email and phone_number and password and repeat_password:
            create_custom_users = CustomUsers()
            create_custom_users.full_name = full_name
            create_custom_users.email = email
            create_custom_users.phone_number = phone_number
            create_custom_users.password = password
            create_custom_users.save()

            return redirect("information")

    context = {"site_title": "Регистрация"}

    return render(request, "registrations.html", context=context)


def information(request):
    context = {
        "site_title": "Информация",
        "full_name": "ФИО",
        "email": "email",
    }

    return render(request, "information.html", context=context)


def metering_devices(request):
    context = {"site_title": "Приборы учета"}

    return render(request, "metering_devices.html", context=context)


def contact(request):
    context = {"site_title": "Контакты"}

    return render(request, "contact.html", context=context)


def accrual_and_payment_history(request):
    context = {"site_title": "Начислено за текущий период"}

    return render(request, "accrual_and_payment_history.html", context=context)


def message(request):
    context = {"site_title": "Начисления"}

    return render(request, "message.html", context=context)


def payment(request):
    context = {"site_title": "Платежи"}

    return render(request, "payment.html", context=context)


def receipts(request):
    context = {"site_title": "Квитанции"}

    return render(request, "receipts.html", context=context)


def notification(request):
    context = {"site_title": "Уведомления"}

    return render(request, "notification.html", context=context)


def consumer_personal_accounts(request):
    context = {"site_title": "Лицевые счета потребителя"}

    return render(request, "consumer_personal_accounts.html", context=context)


def current_period(request):
    context = {"site_title": "Лицевые счета потребителя"}

    return render(request, "current_period.html", context=context)


def assessment(request):
    context = {"site_title": "Начисления"}

    return render(request, "assessment.html", context=context)


def paying(request):
    context = {"site_title": "Платежи"}

    return render(request, "paying.html", context=context)


def get_api_map(request):
    api_maps = os.getenv("API_YANDEX_MAPS")
    context = {"api_maps": api_maps}

    return render(request, "contact.html", context=context)
