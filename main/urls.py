from django.urls import path
from . import views
from .views import HomePage
app_name = 'main'
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
    path('resources/', views.resources, name='resources'),
]