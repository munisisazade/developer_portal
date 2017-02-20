from django.shortcuts import render, redirect,render_to_response
from django.template import RequestContext
from django.urls import  reverse
from django.views.generic import TemplateView
# Create your views here
from news.models import Slider,How_it_works
"""
    Just in case test views
"""


def index(request):
    return redirect(reverse('main-index'))


class TestView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        context['slider'] = Slider.objects.filter(status=True)
        context['how_it'] = How_it_works.objects.all().order_by('id')
        return context
