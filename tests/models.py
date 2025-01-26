import random

from django.db import models

from courses.models import Course,Lesson


class Test(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, related_name='test')
    title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.lesson.course.title} - {self.title}'


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField(max_length=700)
    correctAnswer = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)

    def get_shuffled_options(self):
        options = [self.option1, self.option2, self.option3, self.correctAnswer]
        random.shuffle(options)
        return options

    def __str__(self):
        return self.text
