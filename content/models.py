# -*- coding: UTF-8 -*-
import os
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from redactor.fields import RedactorField
from photologue.models import Gallery
from builtins import str
from django.template.defaultfilters import slugify


class Noticia(models.Model):
    ''' Modelo para noticias '''

    title = models.CharField(u'Título', max_length=500)
    sub_title = models.CharField(u'Subtítulo', max_length=500, null=True, blank=True)

    text = RedactorField(
        verbose_name=u'Texto', allow_file_upload=True,
        allow_image_upload=True, null=True, blank=True
    )
    published_at = models.DateTimeField(u'Data de publicação', null=True)
    expired_at = models.DateTimeField(u'Data de expiração da notícia', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    image = models.ImageField(
        upload_to='noticias/images', verbose_name='Imagem de capa para a Notícia',
        null=True, blank=True
    )
    legend_image = models.CharField('Creditos da imagem de capa para a Notícia', max_length=200, null=True, blank=True)
    tag = models.CharField('Tags para facilitar a busca no site', max_length=100, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Criado por', editable=False)
    notice_origin = models.CharField(u'Fonte da notícia', max_length=200, null=True, blank=True)
    slug = models.SlugField('Identificador', max_length=500, null=False, blank=False, unique=True,
                            help_text="'slug' é um identificador único que será mostrado na url")
    is_public = models.BooleanField(('É Pública ?'), default=True, blank=True,
                                    help_text=('Somente as notícias marcadas como públicas serão apresentadas no site.'))

    class Meta:
        verbose_name = u'Notícia'
        verbose_name_plural = u'Notícias'
        ordering = ['-published_at', 'legend_image']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super(Noticia, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('content:noticia', kwargs={'slug': self.slug})

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

    def exists_image_in_path(self):
        if os.path.exists(self.image.path):
            return True
        else:
            return False


class Comunidade(models.Model):
    ''' Modelo para comunidades '''

    title = models.CharField('Nome da Vila ou Comunidade', max_length=500)
    text = RedactorField(
        verbose_name=u'Sobre a comunidade', allow_file_upload=True,
        allow_image_upload=True, null=True, blank=True
    )
    lat_long = models.CharField('Informe as coordenadas: Latitude e Longitude obtidas através do googleMaps', max_length=500, blank=True, null=False)
    galery = models.ForeignKey(Gallery, verbose_name='Album de Fotos', related_name='galaria', blank=True, null=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Criado por', editable=False, null=True, blank=True)
    slug = models.SlugField('Identificador', max_length=500, null=False, blank=False, unique=True,
                            help_text="'slug' é um identificador único que será mostrado na url")

    class Meta:
        verbose_name = 'Comunidade/Vila'
        verbose_name_plural = 'Comunidades/Vilas'
        ordering = ['title']

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super(Comunidade, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('content:comunidade', kwargs={'slug': self.slug})

    def has_album(self):
        try:
            if self.album:
                return True
            else:
                return False
        except Exception as err:
            print(u"Não foi possivel verificar o arquivo: ", err)
            return False


class YoutubeChannel(models.Model):
    """ Modelo para a página de videos que será integrada com youtube """

    UPLOAD = 'UP'
    PLAYLISTS = 'PL'
    FEATURED = 'FE'

    POPUP = 'PO'
    LINK = 'LK'
    INLINE = 'IN'

    DEFAULT_TAB_CHOICES = (
        (UPLOAD, 'Uploads'),
        (PLAYLISTS, 'Playlists'),
        (FEATURED, 'Featured'),
    )

    VIDEO_DISPLAY_MODE = (
        (POPUP, 'popup'),
        (LINK, 'link'),
        (INLINE, 'inline'),
    )

    title = models.CharField(u'Título', max_length=500,  null=False, blank=False)

    image = models.ImageField(
        upload_to='youtube_channel/images', verbose_name='Imagem de apresentação do canal',
        null=False, blank=False
    )

    slug = models.SlugField('Identificador', max_length=500, null=False, blank=False, unique=True,
                            help_text="'slug' é um identificador único que será mostrado na url")

    channel_link = models.CharField(u'Link do canal', max_length=500,
                                    help_text=u"Link do canal no youtube, exemplo: " \
                                              "https://www.youtube.com/user/crashcourse")

    playlist_link = models.CharField(u'Link da playlist', max_length=500, null=True, blank=True,
                                    help_text=u"Link da playlist no youtube, exemplo: " \
                                              "https://www.youtube.com/playlist?list=PL6_h4dV9kuuIOBDKgxu3q9DpvvJFZ6fB5")

    max_results = models.IntegerField(u'Máximo de resultados por página', default=9, help_text=u"O valor padrão é 9")

    default_tab = models.CharField(
        max_length=2,
        choices=DEFAULT_TAB_CHOICES,
        default=UPLOAD,
    )

    video_display_mode = models.CharField(
        max_length=2,
        choices=VIDEO_DISPLAY_MODE,
        default=POPUP,
    )
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = u'Galeria de vídeos do youtube'
        verbose_name_plural = 'Galerias de vídeos do youtube'
        ordering = ['created_at']

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super(YoutubeChannel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def has_image(self):
        try:
            if self.image and self.image.size > 0:
                return True
            else:
                return False
        except Exception as err:
            print(u"Não foi possivel verificar o arquivo: ", err)
            return False

    def get_absolute_url(self):
        return reverse('content:youtube_playlist', kwargs={'slug': self.slug})

    def exists_image_in_path(self):
        if os.path.exists(self.image.path):
            return True
        else:
            return False


class Timeline(models.Model):
    """ Modelo para eventos da linha do tempo - Página index """

    title = models.CharField(u'Título do evento', max_length=500)
    event_date = models.DateField('Data do evento', null=False, blank=True)
    text = models.TextField(verbose_name='Texto')
    image = models.ImageField(
        upload_to='timeline/images', verbose_name='Imagem de apresentação',
        null=True, blank=True
    )
    legend_image = models.CharField('Legenda da imagem', max_length=200, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Criado por', editable=False, null=True,
                               blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Evento da linha do tempo'
        verbose_name_plural = 'Eventos da linha do tempo'
        ordering = ['event_date']

    def __str__(self):
        return self.title

    def has_image(self):
        try:
            if self.image and self.image.size > 0:
                return True
            else:
                return False
        except Exception as err:
            print(u"Não foi possivel verificar o arquivo: ", err)
            return False

    def exists_image_in_path(self):
        if os.path.exists(self.image.path):
            return True
        else:
            return False


class CategoryFaq(models.Model):

    name = models.CharField('Nome da categoria', max_length=100)
    slug = models.SlugField('Identificador', max_length=500, null=False, blank=False, unique=True,
                            help_text="'slug' é um identificador único que será mostrado na url")

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria de perguntas frequentes'
        verbose_name_plural = 'Categorias de perguntas frequentes'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super(CategoryFaq, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Faq(models.Model):

    question = models.CharField('Pergunta', max_length=500, help_text=u"Pergunta que será apresentada no site")
    answer = models.TextField('Resposta', max_length=1000, help_text=u"Resposta para a pergunta que será apresentada no site")
    category = models.ForeignKey('content.CategoryFaq', related_name='perguntas_frequentes', verbose_name='Categoria')

    slug = models.SlugField('Identificador', max_length=500, null=False, blank=False, unique=True,
                            help_text="'slug' é um identificador único que será mostrado na url")
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Pergunta Frequente'
        verbose_name_plural = 'Perguntas Frequentes'
        ordering = ['question']

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.question)
        super(Faq, self).save(*args, **kwargs)

    def __str__(self):
        return self.question
