from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from courses.models import Course, Lesson, Category



class CourseListView(ListView):
    model = Course
    template_name = 'courses/courses_list.html'
    context_object_name = 'courses'
    # def get_queryset(self):
    #     return Course.objects.all()


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        lessons = Lesson.objects.filter(course=self.object)
        paginator = Paginator(lessons, 5)
        page_num = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
        context = super().get_context_data(**kwargs)
        context['lessons'] = page_obj.object_list
        context['page_obj'] = page_obj
        return context


class CourseCategoryListView(ListView):
    model = Category
    template_name = 'courses/category.html'
    context_object_name = 'categories'

    # def get_context_data(self, **kwargs):
    #     return Course.objects.filter(cat__slug=self.kwargs['sat_slug'])


class CourseCategoryDetailView(ListView):
    template_name = 'courses/category_detail.html'
    context_object_name = 'category_objects'
    # paginate_by = 2


    def get_queryset(self):
        return Course.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(slug=self.kwargs['cat_slug'])
        context['title'] = category.name
        return context

