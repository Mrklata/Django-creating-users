from django.urls import path
from main_site import views

urlpatterns = [
    path('', views.main_site, name="main_site")
]