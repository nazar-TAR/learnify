from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from accounts.forms import LoginUserForm, RegisterUserForm, ProfileForm
from learnify import settings


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'accounts/login.html'
    extra_context = {
        'title': 'Login',
    }

    def get_success_url(self):
        return reverse_lazy('users:index')



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
    extra_context = {
        'title': 'Register',
    }



class ProfileUser(UpdateView):
    model = get_user_model()
    form_class = ProfileForm
    template_name = 'accounts/profile.html'
    extra_context = {
        'title': 'Profile',
        'default_image': settings.DEFAULT_USER_IMAGE,
    }

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self):
        return self.request.user


def index(request):
    return render(request, 'accounts/index.html')


