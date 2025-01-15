from django.http import HttpResponse
from django.shortcuts import render


def login_in_personal_account(request):
    return render(request, "index.html")
