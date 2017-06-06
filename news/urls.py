from django.conf.urls import url
from news.views import TestView, index,AboutView,GalleryView,ContactsView,PrivacyView,CategoryDetailView,ComingSoonView, \
    FacebookInstantArticleRss

urlpatterns = [
    url(r'^$', TestView.as_view(), name='index'),
    url(r'^index.aspx$', index, name='main-index'),
    url(r'^about-us.aspx$', AboutView.as_view(), name='about'),
    url(r'^gallery.aspx$', GalleryView.as_view(), name='gallery'),
    url(r'^contact.aspx$', ContactsView.as_view(), name='contact'),
    url(r'^privacy_policy.aspx$', PrivacyView.as_view(), name='privacy'),
    url(r'^rss.aspx$', FacebookInstantArticleRss.as_view(), name='rss-feed'),
    url(r'^category/(?P<slug>[-\w]+).aspx$',CategoryDetailView.as_view(), name='category'),
    # url(r'^Pages/Default.aspx$', ComingSoonView.as_view(), name='coming-soon'),
    # url(r'^',include('news.urls')),
]
