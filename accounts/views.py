from django.shortcuts import render, redirect
from accounts.models import LangDescription


# Create your views here.


def contact(request):
    return render(request, 'accounts/contact.html')


def skills(request):
    files = LangDescription.objects.all()
    return render(request, 'accounts/skills.html', {'files': files})


def skill_views(request, name):
    skill = LangDescription.objects.get(name__iexact=name)
    return render(request, 'accounts/skill.html', {'skill': skill})
