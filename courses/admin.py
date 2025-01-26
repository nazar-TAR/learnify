from django.contrib import admin

from courses.models import Course, Lesson,Category


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'description', 'instructor', 'cat', 'image']
    readonly_fields = ['slug']
    list_display = ('title', 'description')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'course', 'video_url']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'image']


