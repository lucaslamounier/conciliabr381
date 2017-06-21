#coding=utf-8
"""concilia_BR381 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from core import views
from django.conf.urls.static import static

admin.site.site_title = "Concilia BR 381"
admin.site.site_header = "Concilia BR 381"
admin.site.index_title = 'Painel administrativo do site'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^sobre/$', views.about, name='about'),
    url(r'^duvidas/$', views.duvida, name='faq'),
    url(r'^parceiros/$', views.partners, name='partners'),
    url(r'^conselho-executivo/$', views.conselho_executivo, name='conselho_executivo'),
    url(r'^plano-de-providencias/$', views.plano_providencias, name='plano_providencias'),
    url(r'^criterios-e-regras/$', views.criterios_regras, name='criterios_regras'),
    url(r'^manual-marca/$', views.manual_marca, name='manual_marca'),
    url(r'^conteudos/', include('content.urls', namespace='content')),
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
