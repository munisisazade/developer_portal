from django.conf.urls import url
from news.views import TestView, index,AboutView,GalleryView

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^index.aspx$', TestView.as_view(), name='main-index'),
    url(r'^about-us.aspx$', AboutView.as_view(), name='about'),
    url(r'^gallery.aspx$', GalleryView.as_view(), name='gallery'),
    # url(r'^',include('news.urls')),
]
