from django.contrib import admin
from .models import Noticia
from tinymce.widgets import TinyMCE
from django.core.urlresolvers import reverse

# Register your models here.
class NoticiaAdmin(admin.ModelAdmin):

    list_display = ['title', 'sub_title', 'author', 'created_at', 'updated_at']
    search_fields = ['title', 'sub_title']

admin.site.register(Noticia, NoticiaAdmin)