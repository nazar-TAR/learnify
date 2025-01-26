from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin, CreateView

from courses.models import Course
from .forms import DiscussionForm
from .models import Comment

from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Course, Comment
from .forms import DiscussionForm


def feedback_details(request, slug):
    course = get_object_or_404(Course, slug=slug)

    if request.method == 'POST':
        comment_form = DiscussionForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.course = course
            comment.author = request.user
            comment.save()
            return redirect('discussions:feedback_details', slug=course.slug)
    else:
        comment_form = DiscussionForm()

    comments = Comment.objects.filter(course=course).order_by('-created_at')
    paginator = Paginator(comments, 8)
    page = request.GET.get('page')
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    return render(request, 'discussions/feedback_details.html', {
        'course': course,
        'comments': comments,
        'comment_form': comment_form,
    })





