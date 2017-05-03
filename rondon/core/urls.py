#coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^sobre/$', views.about, name='about'),
    url(r'^comunidades/$', views.community, name='community'),
    url(r'^noticias/$', views.news, name='news'),
]
