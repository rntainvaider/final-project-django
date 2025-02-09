import os

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from dotenv import load_dotenv

from accounts.models import CustomUsers, ServiceOffices

_ = load_dotenv()


def log_in(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        custom_user = CustomUsers.objects.filter(email=email, password=password).first()
        if custom_user:
            login(request, custom_user)
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

            login(request, create_custom_users)

            return redirect("information")

    context = {"site_title": "Регистрация"}

    return render(request, "registration.html", context=context)


@login_required
def settings_user(request):
    user = request.user

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")

    context = {
        "site_title": "Настройки",
        "full_name": "ФИО",
        "email": "email",
    }

    return render(request, "settings_user.html", context=context)


@login_required
def information(request):
    user = request.user

    context = {
        "site_title": "Информация",
        "full_name": user.full_name,
        "email": user.email,
    }

    return render(request, "information.html", context=context)


@login_required
def metering_devices(request):
    context = {"site_title": "Приборы учета"}

    return render(request, "metering_devices.html", context=context)


@login_required
def contact(request):
    api_maps = os.getenv("API_YANDEX_MAPS")

    service_offices = ServiceOffices.objects.first()
    address = service_offices.address
    phone_numbers = service_offices.phone_numbers
    email_address = service_offices.email_address
    latitude = service_offices.latitude
    longitude = service_offices.longitude

    context = {
        "site_title": "Контакты",
        "api_maps": api_maps,
        "address": address,
        "phone_numbers": phone_numbers,
        "email_address": email_address,
        "latitude": latitude,
        "longitude": longitude,
    }

    return render(request, "contact.html", context=context)


@login_required
def accrual_and_payment_history(request):
    context = {"site_title": "Начислено за текущий период"}

    return render(request, "accrual_and_payment_history.html", context=context)


@login_required
def message(request):
    context = {"site_title": "Начисления"}

    return render(request, "message.html", context=context)


@login_required
def payment(request):
    context = {"site_title": "Платежи"}

    return render(request, "payment.html", context=context)


@login_required
def receipts(request):
    context = {"site_title": "Квитанции"}

    return render(request, "receipts.html", context=context)


@login_required
def notification(request):
    context = {"site_title": "Уведомления"}

    return render(request, "notification.html", context=context)


@login_required
def consumer_personal_accounts(request):
    context = {"site_title": "Лицевые счета потребителя"}

    return render(request, "consumer_personal_accounts.html", context=context)


@login_required
def current_period(request):
    context = {"site_title": "Лицевые счета потребителя"}

    return render(request, "current_period.html", context=context)


@login_required
def assessment(request):
    context = {"site_title": "Начисления"}

    return render(request, "assessment.html", context=context)


@login_required
def paying(request):
    context = {"site_title": "Платежи"}

    return render(request, "paying.html", context=context)


@login_required
def log_out(request):
    logout(request)

    return redirect("login")
