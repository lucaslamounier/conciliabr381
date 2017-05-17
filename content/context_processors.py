# coding=utf-8
from .models import Comunidade, Noticia


def comunidades(request):
    return {
        'comunidades': Comunidade.objects.all().order_by('title'),
        'noticias_destaque': Noticia.objects.all().order_by('-published_at')
    }
