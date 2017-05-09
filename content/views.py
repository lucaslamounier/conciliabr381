# coding=utf-8
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.views import generic
from .models import Noticia


# Página de Notícias
class NewsListView(generic.ListView):
    #model = Noticia
    template_name = 'content/news.html'
    context_object_name = 'noticias'
    paginate_by = 3

    def get_queryset(self):
        return Noticia.objects.all().order_by('-published_at')


def noticia(request, pk):
    news = Noticia.objects.get(pk=pk)
    context = {
        'noticia': news,
    }
    return render(request, 'content/noticia.html', context)


# Página de comunidades
class CommunityView(TemplateView):
    template_name = 'content/community.html'


news = NewsListView.as_view()
community = CommunityView.as_view()