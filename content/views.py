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
    paginate_by = 13

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        noticias = context['noticias']
        noticias_destaque_center = []
        noticias_destaque_left = []
        noticias_destaque_right = []
        top_news = []

        if len(noticias) <= 7:
            noticias_destaque_center = noticias
        elif len(noticias) <= 10:
            noticias_destaque_center = noticias[:7]
            noticias_destaque_left = noticias[7:]
        elif len(noticias) > 10:
            noticias_destaque_center = noticias[:7]
            noticias_destaque_left = noticias[7:10]
            noticias_destaque_right = noticias[10:]

        context['noticias_destaque_center'] = noticias_destaque_center
        context['noticias_destaque_left'] = noticias_destaque_left
        context['noticias_destaque_right'] = noticias_destaque_right
        context['noticias_destaque_center_with_image'] = self.get_noticia_destaque_image(context['noticias_destaque_center'])

        for obj in noticias_destaque_center:
            if obj not in context['noticias_destaque_center_with_image']:
                top_news.append(obj)

        context['noticias_destaque_center'] = top_news

        if len(noticias_destaque_center):
            context['noticias_destaque_top'] = noticias_destaque_center[0]
            context['noticias_destaque_center'].pop(0)
        return context

    def get_noticia_destaque_image(self, obj):
        noticias = []
        if len(obj) == 7:
            for item in obj:
                if len(noticias) == 3:
                    break
                if item.has_image():
                    noticias.append(item)
            return noticias
        else:
            return noticias


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