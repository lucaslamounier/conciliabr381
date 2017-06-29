# -*- coding: utf-8 -*-
import re
from django.contrib import admin
from .models import (
        Noticia, Comunidade, Timeline, YoutubeChannel,
        Faq, CategoryFaq
)


# class PropertyImageInline(admin.StackedInline):
#     model = Photo
#     extra = 1


class NoticiaAdmin(admin.ModelAdmin):

    list_display = ['title', 'sub_title', 'author', 'created_at', 'updated_at']
    search_fields = ['title', 'sub_title']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
                obj.author = request.user
        if getattr(obj, 'slug', None) is None:
            text = re.sub(r'[^a-zA-Z0-9 ]', r' ', obj.title)
            obj.slug = text.lower().replace(' ', '-')
        obj.save()


class ComunidadeAdmin(admin.ModelAdmin):

    list_display = ['title', 'author', 'created_at', 'updated_at']
    search_fields = ['title']
    #prepopulated_fields = {"slug": ("title",)}

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        if getattr(obj, 'title', None) is None:
            obj.slug = obj.title
        if getattr(obj, 'slug', None) is None:
            text = re.sub(r'[^a-zA-Z0-9 ]', r' ', obj.title)
            obj.slug = text.lower().replace(' ', '-')
        obj.save()


class TimelineAdmin(admin.ModelAdmin):

    list_display = ['title', 'event_date', 'author']
    search_fields = ['title']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


class YoutubeChannelAdmin(admin.ModelAdmin):

    list_display = ['title', 'channel_link', 'created_at']
    search_fields = ['title']

    def save_model(self, request, obj, form, change):
        """ auto create slug field for url pathner """
        if getattr(obj, 'slug', None) is None:
            try:
                obj.slug = obj.title.replace(' ', '-')
            except Exception as err:
                print(err)
                obj.slug = obj.title
        obj.save()


class FaqAdmin(admin.ModelAdmin):

    list_display = ['question', 'answer', 'category', 'created']
    search_fields = ['question']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'slug', None) is None:
            obj.slug = obj.question.lower().replace(' ', '-')
        obj.save()


class CategoryFaqAdmin(admin.ModelAdmin):

    list_display = ['name', 'created']
    search_fields = ['name']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'slug', None) is None:
            obj.slug = obj.name.lower().replace(' ', '-')
        obj.save()


admin.site.register(Comunidade, ComunidadeAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Timeline, TimelineAdmin)
admin.site.register(YoutubeChannel, YoutubeChannelAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(CategoryFaq, CategoryFaqAdmin)
