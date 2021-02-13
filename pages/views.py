from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return render(request, 'home.html', {})


def contact_view(request):
    html_str = "<h1>Contact Page</h1>"
    return HttpResponse(html_str)


def about_view(request):
    return render(request, 'about.html', {})


def social_view(request):
    html_str = "<h1>Social Page</h1>"
    return HttpResponse(html_str)
