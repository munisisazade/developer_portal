from django.conf.urls import url
from news.views import TestView, index,AboutView,GalleryView,ContactsView,PrivacyView

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^index.aspx$', TestView.as_view(), name='main-index'),
    url(r'^about-us.aspx$', AboutView.as_view(), name='about'),
    url(r'^gallery.aspx$', GalleryView.as_view(), name='gallery'),
    url(r'^contact.aspx$', ContactsView.as_view(), name='contact'),
    url(r'^privacy_policy.aspx$', PrivacyView.as_view(), name='privacy'),
    # url(r'^',include('news.urls')),
]
