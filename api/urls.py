from django.conf.urls import url, include
from api.views import UserList,BrandDetail,NewsList,ArticleDetail


urlpatterns = [
    url(r'^user/(?P<pk>[0-9]+)/$', BrandDetail.as_view(), name='user-detail'),
    url(r'^user-list/$', UserList.as_view(), name='user-list'),
    url(r'^news-list/$', NewsList.as_view(), name='news-list'),
    url(r'^article/(?P<pk>[0-9]+)$', ArticleDetail.as_view(), name='article-detail'),

]