from django.http import HttpResponse
from django.shortcuts import redirect, render

from accounts.models import CustomUsers


def login_to_personal_account(request) -> HttpResponse:
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        custom_user = CustomUsers.objects.filter(email=email, password=password).first()
        if custom_user:
            return redirect("index.html")
        else:
            context = {
                "site_title": "Авторизация - Личный кабинет",
            }

            return render(request, "login_to_personal_account.html", context=context)

    context = {
        "site_title": "Авторизация - Личный кабинет",
    }
    return render(request, "login_to_personal_account.html", context=context)


def registration(request) -> HttpResponse:
    context = {"site_title": "Регистрация - Личный кабинет"}

    return render(request, "registration.html", context=context)
