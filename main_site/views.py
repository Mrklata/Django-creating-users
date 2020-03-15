from django.shortcuts import render
import datetime
# Create your views here.


def main_site(request):
    born = datetime.date(1998, 8, 2)
    today = datetime.date.today()
    age = today.year - born.year

    return render(request, 'main_site/main_site.html', {'age': age})
