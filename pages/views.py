from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return render(request, 'home.html', {})


def contact_view(request):
    html_str = "<h1>Contact Page</h1>"
    return HttpResponse(html_str)


def about_view(request):
    my_context = {
        'my_text': "this is about us",
        'my_number': 123,
        'my_html': '<h1>I am so tired.</h1>',
        'my_list': [21, 'RM', 'SUGA', 'J-HOPE'],
    }
    return render(request, 'about.html', my_context)


def social_view(request):
    html_str = "<h1>Social Page</h1>"
    return HttpResponse(html_str)
