from django.shortcuts import render, redirect
from accounts.models import LangDescription


# Create your views here.


def contact(request):
    return render(request, 'accounts/contact.html')


def skills(request):
    return render(request, 'accounts/skills.html')


def python(request):
    file = LangDescription.objects.filter(selection='Python')[0]
    return render(request, 'accounts/python.html', {'file': file})


def django(request):
    file = LangDescription.objects.filter(selection='Django')[0]
    return render(request, 'accounts/django.html', {'file': file})


def html(request):
    file = LangDescription.objects.filter(selection='HTML')[0]
    return render(request, 'accounts/html.html', {'file': file})


def css(request):
    file = LangDescription.objects.filter(selection='CSS')[0]
    return render(request, 'accounts/css.html', {'file': file})
