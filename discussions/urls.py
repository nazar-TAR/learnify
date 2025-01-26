from django.urls import path
from . import views
app_name = 'discussions'
urlpatterns = [
    path('<slug:slug>/', views.feedback_details, name='feedback_details'),
]