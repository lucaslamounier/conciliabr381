# coding=utf-8
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.views import generic
from .models import Noticia, Comunidade
from django.db.models import Q

# Página de Notícias
class NewsListView(generic.ListView):
    model = Noticia
    template_name = 'content/news.html'
    # context_object_name = 'noticias'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['noticias'] = Noticia.objects.all().order_by('-published_at')
        context['noticias'] = Noticia.objects.filter(image='').order_by('-published_at')
        context['noticias_carrousel'] = Noticia.objects.filter(~Q(image='')).order_by('-published_at')
        return context

# Página de Notícia
def noticia(request, pk):
    news = Noticia.objects.get(pk=pk)
    context = {
        'noticia': news,
    }
    return render(request, 'content/_noticia.html', context)


# Página de comunidade
def comunidade(request, pk):
    community = Comunidade.objects.get(pk=pk)
    context = {
        'comunidade': community,
    }
    return render(request, 'content/_comunidade.html', context)


# Página de comunidades
class CommunityView(TemplateView):
    template_name = 'content/communitys.html'


news = NewsListView.as_view()
community = CommunityView.as_view()