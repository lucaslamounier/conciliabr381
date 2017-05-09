from django.contrib import admin
from .models import Noticia, Comunidade, Album, Photo
from tinymce.widgets import TinyMCE
from django.core.urlresolvers import reverse


class NoticiaAdmin(admin.ModelAdmin):

    list_display = ['title', 'sub_title', 'author', 'created_at', 'updated_at']
    search_fields = ['title', 'sub_title']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
                obj.author = request.user
        obj.save()


class ComunidadeAdmin(admin.ModelAdmin):

    list_display = ['title', 'author', 'created_at', 'updated_at']
    search_fields = ['title']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        if getattr(obj, 'title', None) is None:
            obj.slug = obj.title
        obj.save()


class AlbumAdmin(admin.ModelAdmin):

    list_display = ['name', 'author', 'date_created']
    search_fields = ['name']

    def save_model(self, request, obj, form, change):
        obj.slug = obj.name
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


class PhotoAdmin(admin.ModelAdmin):

    list_display = ['title', 'legend', 'album', 'author', 'date_created']
    search_fields = ['title']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


admin.site.register(Comunidade, ComunidadeAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)