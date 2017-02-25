from django.shortcuts import render, redirect,render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.urls import  reverse
from django.views.generic import TemplateView,DetailView
# Create your views here
from news.models import Slider,How_it_works,ArticleCategory,Contact_us,ArticleCategory,Article,RelationCategoryArticle,ArticleImages,Haqqimizda
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
        context['feed'] = Article.objects.filter(status=True,home_page_status=True)
        return context

class AboutView(TemplateAllData):
    template_name = 'index-1.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['contact_object'] = Haqqimizda.objects.all()[0]
        return context

class GalleryView(TemplateAllData):
    template_name = 'index-2.html'

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        context['albom'] = ArticleImages.objects.all()
        return context

class ContactsView(TemplateAllData):
    template_name = 'index-4.html'

class PrivacyView(TemplateAllData):
    template_name = 'index-5.html'


class CategoryDetailView(DetailView):
    model = ArticleCategory
    template_name = 'index-3.html'


    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['categorys'] = ArticleCategory.objects.all()
        context['contact'] = Contact_us.objects.all()
        context['cat_feed'] = RelationCategoryArticle.objects.filter(category_obj__slug=self.kwargs.get('slug'),article_obj__status=True)
        return context


class ComingSoonView(TemplateView):
    template_name = 'comin-soon.html'