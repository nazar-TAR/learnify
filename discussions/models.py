from django.db import models
from courses.models import Course
from accounts.models import User


class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='feedbacks')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('feedback')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback from {self.author} to {self.course}'
