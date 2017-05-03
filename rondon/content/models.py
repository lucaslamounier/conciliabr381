# coding=utf-8
from django.db import models
from tinymce.models import HTMLField
from django.conf import settings

class Noticia(models.Model):

    title = models.CharField('Título', max_length=500)
    sub_title = models.CharField('Subtítulo', max_length=500)
    text = HTMLField(verbose_name='texto')
    published_at = models.DateTimeField('Data de publicação', null=True)
    expired_at = models.DateTimeField('Data de expiração da notícia', null=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    image = models.ImageField(
        upload_to='noticias/images', verbose_name='Imagem',
        null=True, blank=True
    )
    legend_image = models.CharField('Legenda da imagem', max_length=200, null=True)
    tag = models.CharField('Tags para facilitar a busca no site', max_length=100, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Criado por')

    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
        ordering = ['title']

    def __str__(self):
            return self.title

