#coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^noticias/$', views.news, name='noticias'),
    url(r'^perguntas-frequentes/$', views.perguntas_frequentes, name='perguntas-frequentes'),
    url(r'^acervo/videos/$', views.videos, name='videos'),
    url(r'^acervo/videos/(?P<slug>[\w_-]+)/$', views.youtube_playlist_view, name='youtube_playlist'),
    url(r'^acervo/galeria/$', views.galeria, name='galeria'),
    url(r'^acervo/galeria/(?P<slug>[\-\d\w]+)/$', views.geleria_detalhe, name='galery-detail'),
    url(r'^noticia/(?P<pk>[\w_-]+)/$', views.noticia, name='noticia'),
    url(r'^comunidades/$', views.community, name='comunidades'),
    url(r'^comunidade/(?P<pk>[\w_-]+)/$', views.comunidade, name='comunidade'),
]
