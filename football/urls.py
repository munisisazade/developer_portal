from django.conf.urls import url
from django.views.generic import TemplateView
from football.views import ScreapyView

urlpatterns = [
    url(r'^$', ScreapyView.as_view(),name='home'),
    url(r'^index.html/$', TemplateView.as_view(template_name='html/index.html'),name='home'),
    url(r'^404.html/$', TemplateView.as_view(template_name='html/404.html'), name='404'),
    url(r'^checkout.html/$', TemplateView.as_view(template_name='html/checkout.html'),name='checkout'),
    url(r'^club.html/$', TemplateView.as_view(template_name='html/club.html'), name='club'),
    url(r'^contact.html/$', TemplateView.as_view(template_name='html/contact.html'),name='contact'),
    url(r'^standings.html/$', TemplateView.as_view(template_name='html/standings.html'), name='standings'),
    url(r'^faq.html/$', TemplateView.as_view(template_name='html/faq.html'),name='faq'),
    url(r'^login.html/$', TemplateView.as_view(template_name='html/login.html'), name='login'),
    url(r'^news.html/$', TemplateView.as_view(template_name='html/news.html'),name='news'),
    url(r'^news-single.html/$', TemplateView.as_view(template_name='html/news-single.html'), name='news-single'),
    url(r'^players.html/$', TemplateView.as_view(template_name='html/players.html'),name='players'),
    url(r'^product-details.html/$', TemplateView.as_view(template_name='html/product-details.html'), name='product-details'),
    url(r'^register.html/$', TemplateView.as_view(template_name='html/register.html'),name='register'),
    url(r'^result.html/$', TemplateView.as_view(template_name='html/result.html'), name='result'),
    url(r'^schedule.html/$', TemplateView.as_view(template_name='html/schedule.html'), name='schedule'),
    url(r'^shop.html/$', TemplateView.as_view(template_name='html/shop.html'), name='shop'),
    url(r'^shopping-cart.html/$', TemplateView.as_view(template_name='html/shopping-cart.html'),name='shopping-cart'),
    url(r'^standings.html/$', TemplateView.as_view(template_name='html/standings.html'), name='standings'),
    url(r'^testimonial.html/$', TemplateView.as_view(template_name='html/testimonial.html'), name='testimonial'),
    url(r'^top-scores.html/$', TemplateView.as_view(template_name='html/top-scores.html'), name='top-scores'),
    url(r'^wishlist.html/$', TemplateView.as_view(template_name='html/wishlist.html'),name='wishlist'),

    # url(r'^article/(?P<pk>[0-9]+)$', ArticleDetail.as_view(), name='article-detail'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api-token-auth/', obtain_jwt_token),
]