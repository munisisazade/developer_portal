from django.shortcuts import render, redirect,render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.urls import  reverse
from django.views.generic import TemplateView
# Create your views here
from news.models import Slider,How_it_works,ArticleCategory,Contact_us
"""
    Just in case test views
"""


def index(request):
    return redirect(reverse('main-index'))

class TemplateAllData(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(TemplateAllData, self).get_context_data(**kwargs)
        context['categorys'] = ArticleCategory.objects.all()
        context['contact'] = Contact_us.objects.all()
        return context




class TestView(TemplateAllData):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        context['slider'] = Slider.objects.filter(status=True)
        context['how_it'] = How_it_works.objects.all().order_by('id')
        return context

class AboutView(TemplateAllData):
    template_name = 'index-1.html'

class GalleryView(TemplateAllData):
    template_name = 'index-2.html'

class ContactsView(TemplateAllData):
    template_name = 'index-4.html'

class PrivacyView(TemplateAllData):
    template_name = 'index-5.html'