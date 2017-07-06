# -*- coding: utf-8 -*-
import re
from django.contrib import admin
from .models import (
        Noticia, Comunidade, Timeline, YoutubeChannel,
        Faq, CategoryFaq
)


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'author', 'created_at', 'updated_at']
    search_fields = ['title', 'sub_title']
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
                obj.author = request.user
        obj.save()


class ComunidadeAdmin(admin.ModelAdmin):

    list_display = ['title', 'author', 'created_at', 'updated_at']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'text')
        }),
        ('Localização', {
            'fields': ('lat', 'long')
        }),
        ('Galaria de Fotos', {
            'fields': ('galery',)
        })
    )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
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
    prepopulated_fields = {'slug': ('title',)}


class FaqAdmin(admin.ModelAdmin):

    list_display = ['question', 'answer', 'category', 'created']
    search_fields = ['question']


class CategoryFaqAdmin(admin.ModelAdmin):

    list_display = ['name', 'created']
    search_fields = ['name']


admin.site.register(Comunidade, ComunidadeAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Timeline, TimelineAdmin)
admin.site.register(YoutubeChannel, YoutubeChannelAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(CategoryFaq, CategoryFaqAdmin)
