# coding=utf-8
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.views import generic
from django.views.generic.detail import DetailView
from .models import Noticia, Comunidade, YoutubeChannel, CategoryFaq
from django.db.models import Q
from photologue.models import Gallery


# Página de Notícias
class NewsListView(generic.ListView):
    model = Noticia
    template_name = 'content/news.html'
    context_object_name = 'noticias'
    paginate_by = 12

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['noticias'] = Noticia.objects.all().order_by('-published_at')
    #     #context['noticias'] = Noticia.objects.filter(image='').order_by('-published_at')
    #     #context['noticias_carrousel'] = Noticia.objects.filter(~Q(image='')).order_by('-published_at')
    #     return context

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


# Página de videos
class VideosView(generic.ListView):
    model = YoutubeChannel
    template_name = 'content/videos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['channels'] = YoutubeChannel.objects.all()
        return context


# Página de galeria de fotos
class GaleryListVew(generic.ListView):
    model = Gallery
    template_name = 'content/gallery.html'
    queryset = Gallery.objects.on_site().is_public()
    context_object_name = 'galeria_fotos'
    paginate_by = 20


class GalleryDetailView(DetailView):
    queryset = Gallery.objects.on_site().is_public()
    template_name = 'content/gallery_detail.html'


def youtube_playlist_view(request, slug):
    play_list = YoutubeChannel.objects.get(slug=slug)
    context = {
        'playlist': play_list,
    }
    return render(request, 'content/video_detail.html', context)


# Página de dúvidas
class PerguntasFrequentesView(generic.ListView):
    queryset = CategoryFaq.objects.all()
    context_object_name = 'categorias_perguntas_frequentes'
    template_name = 'content/perguntas_frequentes.html'


news = NewsListView.as_view()
community = CommunityView.as_view()
videos = VideosView.as_view()
galeria = GaleryListVew.as_view()
geleria_detalhe = GalleryDetailView.as_view()
perguntas_frequentes = PerguntasFrequentesView.as_view()