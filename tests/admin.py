from django.contrib import admin

from .models import Test, Question


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    fields = ['lesson', 'title']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ['test', 'text', 'correctAnswer', 'option1', 'option2', 'option3']
