#coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^noticias/$', views.news, name='noticias'),
    url(r'^noticia/(?P<pk>[\w_-]+)/$', views.noticia, name='noticia'),
    url(r'^comunidades/$', views.community, name='comunidades'),
]
