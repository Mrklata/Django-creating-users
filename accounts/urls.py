from django.urls import path
from accounts import views
urlpatterns = [
    path('contact/', views.contact, name="contact"),
    path('skills/', views.skills, name="skills"),
    path('skills/<str:name>/', views.skill_views, name='skill'),
]
