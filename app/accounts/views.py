from django.shortcuts import redirect, render

from accounts.models import CustomUsers


def login_to_personal_account(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        custom_user = CustomUsers.objects.filter(email=email, password=password).first()
        if custom_user:
            return redirect("informations")
        else:
            context = {
                "site_title": "Авторизация",
            }

            return render(request, "login_to_personal_account.html", context=context)

    context = {
        "site_title": "Авторизация",
    }
    return render(request, "login_to_personal_account.html", context=context)


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

            return redirect("informations")

    context = {"site_title": "Регистрация"}

    return render(request, "registrations.html", context=context)


def informations(request):
    context = {"site_title": "Информация"}

    return render(request, "informations.html", context=context)


def metering_devices(request):
    context = {"site_title": "Приборы учета"}

    return render(request, "metering_devices.html", context=context)


def contacts(request):
    context = {"site_title": "Контакты"}

    return render(request, "contacts.html", context=context)
