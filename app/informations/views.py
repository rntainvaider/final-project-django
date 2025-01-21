from django.shortcuts import render


def information(request):
    context = {"site_title": "Информация"}

    return render(request, "information.html", context=context)
