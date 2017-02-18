from django.shortcuts import render, redirect
from django.urls import  reverse
from django.views.generic import TemplateView
# Create your views here
"""
    Just in case test views
"""


def index(request):
    return redirect(reverse('main-index'))


class TestView(TemplateView):
    template_name = 'index.html'
