# -*- coding: UTF-8 -*-
from django.db import models
from tinymce.models import HTMLField
from django.conf import settings
from django.core.urlresolvers import reverse
from builtins import str


class Album(models.Model):

    ''' Modelo para albuns '''

    name = models.CharField(u'Título do album', max_length=300)
    slug = models.SlugField(editable=False)
    description = models.CharField(u'Descrição do album', max_length=300, null=True, blank=True)
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

    ''' Modelo para fotos '''

    title = models.CharField(u'Título', max_length=300)
    legend = models.TextField('Legenda', blank=True, null=True)
    date_created = models.DateTimeField('Criado em', auto_now_add=True)
    date_modified = models.DateTimeField('Modificado em', auto_now=True)
    image = models.ImageField(upload_to='fotos/%Y/%m')
    album = models.ForeignKey(Album, verbose_name='Album', related_name='fotos')
    photographer = models.CharField('Nome do Fotografo', max_length=200, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Criado por', editable=False, null=True, blank=True)

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
        ordering = ['title']

    def __str__(self):
        return self.title


class Noticia(models.Model):

    ''' Modelo para noticias '''

    title = models.CharField(u'Título', max_length=500)
    sub_title = models.CharField(u'Subtítulo', max_length=500)
    text = HTMLField(verbose_name='texto')
    published_at = models.DateTimeField(u'Data de publicação', null=True)
    expired_at = models.DateTimeField(u'Data de expiração da notícia', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    image = models.ImageField(
        upload_to='noticias/images', verbose_name='Imagem',
        null=True, blank=True
    )
    legend_image = models.CharField('Legenda da imagem', max_length=200, null=True, blank=True)
    tag = models.CharField('Tags para facilitar a busca no site', max_length=100, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Criado por', editable=False)
    notice_origin = models.CharField(u'Fonte da notícia', max_length=200, null=True, blank=True)
    album = models.ForeignKey(Album, verbose_name='Album de Fotos', related_name='album_noticia', blank=True, null=True)

    class Meta:
        verbose_name = u'Notícia'
        verbose_name_plural = u'Notícias'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('content:noticia', kwargs={'pk': self.pk})

    def has_image(self):
        try:
            if self.image and self.image.size > 0:
                return True
            else:
                return False
        except Exception as err:
            print(u"Não foi possivel verificar o arquivo: ", err)
            return False

    def has_album(self):
        try:
            if self.album:
                return True
            else:
                return False
        except Exception as err:
            print(u"Não foi possivel verificar o arquivo: ", err)
            return False


class Comunidade(models.Model):

    ''' Modelo para comunidades '''

    title = models.CharField('Nome da Vila ou Comunidade', max_length=500)
    about = HTMLField(verbose_name='Sobre')
    lat_long = models.CharField('Informe as coordenadas: Latitude e Longitude obtidas através do googleMaps', max_length=500, blank=True, null=False)
    album = models.ForeignKey(Album, verbose_name='Album de Fotos', related_name='album', blank=True, null=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Criado por', editable=False, null=True, blank=True)

    class Meta:
        verbose_name = 'Comunidade/Vila'
        verbose_name_plural = 'Comunidades/Vilas'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('content:comunidade', kwargs={'pk': self.pk})

    def has_album(self):
        try:
            if self.album:
                return True
            else:
                return False
        except Exception as err:
            print(u"Não foi possivel verificar o arquivo: ", err)
            return False


class Timeline(models.Model):

    """ Modelo para eventos da linha do tempo - Página index """

    title = models.CharField(u'Título do evento', max_length=500)
    event_date = models.DateField('Data do evento',  null=False, blank=True)
    text = models.TextField(verbose_name='Texto')
    image = models.ImageField(
        upload_to='timeline/images', verbose_name='Imagem de apresentação',
        null=True, blank=True
    )
    legend_image = models.CharField('Legenda da imagem', max_length=200, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Criado por', editable=False, null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Evento da linha do tempo'
        verbose_name_plural = 'Eventos da linha do tempo'
        ordering = ['-event_date']

    def __str__(self):
        return '[%s] - %s' % (self.event_date, self.title)

    def has_image(self):
        try:
            if self.image and self.image.size > 0:
                return True
            else:
                return False
        except Exception as err:
            print(u"Não foi possivel verificar o arquivo: ", err)
            return False
