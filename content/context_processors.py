# coding=utf-8

from .models import Comunidade, Noticia
from django.conf import settings


def comunidades(request):
    return {
        'comunidades': Comunidade.objects.all().order_by('title'),
        'YOUTUBE_API_KEY': settings.YOUTUBE_API_KEY,
    }
