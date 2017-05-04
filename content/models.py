# coding=utf-8
from django.db import models
from tinymce.models import HTMLField
from django.conf import settings


class Noticia(models.Model):
    title = models.CharField('Título', max_length=500)
    sub_title = models.CharField('Subtítulo', max_length=500)
    text = HTMLField(verbose_name='texto')
    published_at = models.DateTimeField('Data de publicação', null=True)
    expired_at = models.DateTimeField('Data de expiração da notícia', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    image = models.ImageField(
        upload_to='noticias/images', verbose_name='Imagem',
        null=True, blank=True
    )
    legend_image = models.CharField('Legenda da imagem', max_length=200, null=True)
    tag = models.CharField('Tags para facilitar a busca no site', max_length=100, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Criado por', editable=False)

    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'
        ordering = ['title']

    def __str__(self):
        return self.title


class Album(models.Model):
    name = models.CharField('Título do album', max_length=300)
    slug = models.SlugField(editable=False)
    description = models.CharField('Descrição do album', max_length=300, null=True, blank=True)
    date_created = models.DateTimeField('Criado em', auto_now_add=True)
    date_modified = models.DateTimeField('Modificado em', auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Criado por', editable=False, null=True, blank=True)

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albuns'
        ordering = ['name']

    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField('Título', max_length=300)
    legend = models.TextField('Legenda', blank=True, null=True)
    date_created = models.DateTimeField('Criado em', auto_now_add=True)
    date_modified = models.DateTimeField('Modificado em', auto_now=True)
    image = models.ImageField(upload_to='fotos/%Y/%m')
    album = models.ForeignKey(Album, verbose_name='Album')
    photographer = models.CharField('Nome do Fotografo', max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Criado por', editable=False, null=True, blank=True)

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
        ordering = ['title']

    def __str__(self):
        return self.title


class Comunidade(models.Model):

    title = models.CharField('Nome da Vila ou Comunidade', max_length=500)
    about = HTMLField(verbose_name='Sobre')
    num_latitude = models.FloatField('Latitude', blank=True, null=True)
    num_longitude = models.FloatField('Longitude', blank=True, null=True)
    album = models.ForeignKey(Album, verbose_name='Album de Fotos', blank=True, null=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Criado por', editable=False, null=True, blank=True)

    class Meta:
        verbose_name = 'Comunidade/Vila'
        verbose_name_plural = 'Comunidades/Vilas'
        ordering = ['title']

    def __str__(self):
        return self.title


