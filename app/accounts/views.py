from django.shortcuts import render


def login_to_personal_account(request):
    return render(request, "login_to_personal_account.html")


def registration(request):
    return render(request, "registration.html")
