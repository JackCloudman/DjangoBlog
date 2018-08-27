from django.conf.urls import include, url
from django.views.generic.base import RedirectView
from django.urls import path
from . import views
urlpatterns = [
    url(r'^$', views.home),
    url(r'^page/$', RedirectView.as_view(url='/', permanent=False)),
    url(r'^page/(?P<page>[0-9]+)/$', views.home, name='page_list'),
    url(r'^post/(?P<pk>[0-9]+)/(?P<title>[-a-zA-Z0-9_]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]