from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from api.views import UserList,BrandDetail,NewsList,ArticleDetail


urlpatterns = [
    url(r'^user/(?P<pk>[0-9]+)/$', BrandDetail.as_view(), name='user-detail'),
    url(r'^user-list/$', UserList.as_view(), name='user-list'),
    url(r'^news-list/$', NewsList.as_view(), name='news-list'),
    url(r'^article/(?P<pk>[0-9]+)$', ArticleDetail.as_view(), name='article-detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
]