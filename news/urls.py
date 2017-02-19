from django.conf.urls import url
from news.views import TestView, index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^index.aspx$', TestView.as_view(), name='main-index')
    # url(r'^',include('news.urls')),
]
