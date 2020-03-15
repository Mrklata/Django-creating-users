from django.urls import path
from accounts import views
urlpatterns = [
    path('contact/', views.contact, name="contact"),
    path('skills/', views.skills, name="skills"),
    path('skills/python', views.python, name='python'),
    path('skills/django', views.django, name='django'),
    path('skills/html', views.html, name='html'),
    path('skills/css', views.css, name='css'),

]