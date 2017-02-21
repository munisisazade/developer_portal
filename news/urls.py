from django.conf.urls import url
from news.views import TestView, index,AboutView

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^index.aspx$', TestView.as_view(), name='main-index'),
    url(r'^about-us.aspx$', AboutView.as_view(), name='about'),
    # url(r'^',include('news.urls')),
]
