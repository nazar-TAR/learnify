from django.urls import path
from . import views

app_name = 'tests'

urlpatterns = [
    path('lesson/<int:lesson_id>/test/', views.TestDetailView.as_view(), name='test_detail'),
]