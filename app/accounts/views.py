from django.shortcuts import render


def login_in_personal_account(request):
    return render(request, "login_to_personal_account.html")
