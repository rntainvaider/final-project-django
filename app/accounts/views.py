import os

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from dotenv import load_dotenv

from accounts.models import CustomUsers, Receipt

_ = load_dotenv()


# def log_in(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")

#         custom_user = CustomUsers.objects.filter(email=email, password=password).first()
#         if custom_user:
#             login(request, custom_user)
#             return redirect("information")
#         else:
#             context = {
#                 "site_title": "Авторизация",
#             }

#             return render(request, "login.html", context=context)

#     context = {
#         "site_title": "Авторизация",
#     }
#     return render(request, "login.html", context=context)


def login(request):
    context = {
        "page_title": "Авторизация",
    }

    return render(request, "login.html", context=context)


def registration(request):
    context = {
        "page_title": "Регистрация",
    }

    return render(request, "registration.html", context=context)


# def registration(request):
#     if request.method == "POST":
#         full_name = request.POST.get("full_name")
#         email = request.POST.get("email")
#         phone_number = request.POST.get("phone")
#         password = request.POST.get("password")
#         repeat_password = request.POST.get("repeat_password")

#         if full_name and email and phone_number and password and repeat_password:
#             create_custom_users = CustomUsers()
#             create_custom_users.full_name = full_name
#             create_custom_users.email = email
#             create_custom_users.phone_number = phone_number
#             create_custom_users.password = password
#             create_custom_users.save()

#             login(request, create_custom_users)

#             return redirect("information")

#     context = {"site_title": "Регистрация"}

#     return render(request, "registration.html", context=context)


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

    service_office = user.service_office
    work_schedule = user.work_schedule

    office_address = service_office.address
    office_phone_number = service_office.phone_numbers
    office_email = service_office.email_address
    office_latitude = service_office.latitude
    office_longitude = service_office.longitude

    work_schedule_days = work_schedule.days_of_week.all()

    context = {
        "site_title": "Информация",
        "full_name": user.full_name,
        "email": user.email,
        "office_address": office_address,
        "phone_number": office_phone_number,
        "office_email": office_email,
        "work_schedule_days": work_schedule_days,
        "office_latitude": office_latitude,
        "office_longitude": office_longitude,
    }

    return render(request, "information.html", context=context)


@login_required
def metering_devices(request):
    user = request.user

    context = {
        "site_title": "Приборы учета",
        "full_name": user.full_name,
        "email": user.email,
    }

    return render(request, "metering_devices.html", context=context)


@login_required
def contact(request):
    user = request.user
    service_office = user.service_office
    work_schedule = user.work_schedule

    office_address = service_office.address
    office_phone_number = service_office.phone_numbers
    office_email = service_office.email_address
    office_latitude = service_office.latitude
    office_longitude = service_office.longitude

    work_schedule_days = work_schedule.days_of_week.all()

    context = {
        "site_title": "Контакты",
        "full_name": user.full_name,
        "email": user.email,
        "office_address": office_address,
        "phone_number": office_phone_number,
        "office_email": office_email,
        "work_schedule_days": work_schedule_days,
        "office_latitude": office_latitude,
        "office_longitude": office_longitude,
    }

    return render(request, "contact.html", context=context)


@login_required
def accrual_and_payment_history(request):
    user = request.user

    context = {
        "site_title": "Начислено за текущий период",
        "full_name": user.full_name,
        "email": user.email,
    }

    return render(request, "accrual_and_payment_history.html", context=context)


@login_required
def message(request):
    user = request.user

    context = {
        "site_title": "Начисления",
        "full_name": user.full_name,
        "email": user.email,
    }

    return render(request, "message.html", context=context)


def get_pagination_range(page_obj, num_pages_to_display: int = 5):
    current_page = page_obj.number
    total_pages = page_obj.paginator.num_pages
    half_range = num_pages_to_display // 2

    if total_pages <= num_pages_to_display:
        return range(1, total_pages + 1)

    start_page = max(current_page - half_range, 1)
    end_page = min(current_page + half_range, total_pages)

    if start_page > 1:
        if end_page < total_pages:
            return list(range(start_page, end_page + 1)) + ["...", total_pages]
        # return list(range(start_page, end_page + 1))
        return [1, "..."] + list(range(start_page, end_page + 1))
    if end_page < total_pages:
        # return [1, "..."] + list(range(start_page, end_page + 1))
        # return list(range(start_page, end_page + 1))
        return list(range(start_page, end_page + 1)) + ["...", total_pages]
    # return [1, "..."] + list(range(start_page, end_page + 1))
    # return list(range(start_page, end_page + 1))


@login_required
def receipts(request):
    user = request.user

    data = Receipt.objects.all()
    paginator = Paginator(data, 10)

    # Получение текущей страницы из параметров GET
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    pagination_range = get_pagination_range(page_obj)

    context = {
        "site_title": "Квитанции",
        "full_name": user.full_name,
        "email": user.email,
        "page_obj": page_obj,
        "pagination_range": pagination_range,
    }

    return render(request, "receipts.html", context=context)


@login_required
def notification(request):
    user = request.user

    context = {
        "site_title": "Уведомления",
        "full_name": user.full_name,
        "email": user.email,
    }

    return render(request, "notification.html", context=context)


@login_required
def consumer_personal_accounts(request):
    user = request.user

    context = {
        "site_title": "Лицевые счета потребителя",
        "full_name": user.full_name,
        "email": user.email,
    }

    return render(request, "consumer_personal_accounts.html", context=context)


@login_required
def payment(request):
    user = request.user

    context = {
        "site_title": "Платежи",
        "full_name": user.full_name,
        "email": user.email,
    }

    return render(request, "payment.html", context=context)


@login_required
def current_period(request):
    user = request.user

    context = {
        "site_title": "Лицевые счета потребителя",
        "full_name": user.full_name,
        "email": user.email,
    }

    return render(request, "current_period.html", context=context)


@login_required
def assessment(request):
    user = request.user

    context = {
        "site_title": "Начисления",
        "full_name": user.full_name,
        "email": user.email,
    }

    return render(request, "assessment.html", context=context)


@login_required
def paying(request):
    user = request.user

    context = {
        "site_title": "Платежи",
        "full_name": user.full_name,
        "email": user.email,
    }

    return render(request, "paying.html", context=context)


@login_required
def get_api_map(request):
    api_maps = os.getenv("API_YANDEX_MAPS")
    context = {
        "api_maps": api_maps,
        "latitude": 55.751574,
        "longitude": 37.573856,
    }

    return render(request, "contact.html", context=context)


@login_required
def log_out(request):
    logout(request)

    return redirect("login")
