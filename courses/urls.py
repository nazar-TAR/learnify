from django.urls import path
from . import views
from .views import CourseListView, CourseDetailView, CourseCategoryListView, CourseCategoryDetailView

app_name = 'courses'
urlpatterns = [
    # path('', CourseListView.as_view(), name='course_list'),
    path('category/', CourseCategoryListView.as_view(), name='course_category_list'),
    path('category/<slug:cat_slug>/', CourseCategoryDetailView.as_view(), name='course_category_detail'),
    path('<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),

]