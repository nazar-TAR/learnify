from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'main/home.html'


def about(request):
    return HttpResponse('About Us')

def contact(request):
    return HttpResponse('Contact Us')

def pricing(request):
    return HttpResponse('Privacy Policy')

def resources(request):
    return HttpResponse('Resources')