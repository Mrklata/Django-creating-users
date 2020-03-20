from django.shortcuts import render, redirect
from accounts.models import LangDescription


# Create your views here.


def contact(request):
    return render(request, 'accounts/contact.html')


def skills(request):
    return render(request, 'accounts/skills.html')


def python(request):
    file = LangDescription.objects.get(selection='Python')
    return render(request, 'accounts/python.html', {'file': file})


def django(request):
    file = LangDescription.objects.get(selection='Django')
    return render(request, 'accounts/django.html', {'file': file})


def html(request):
    file = LangDescription.objects.get(selection='HTML')
    return render(request, 'accounts/html.html', {'file': file})


def css(request):
    file = LangDescription.objects.get(selection='CSS')
    return render(request, 'accounts/css.html', {'file': file})
