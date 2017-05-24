# coding=utf-8
from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.generic import View, TemplateView, ListView
from content.models import Noticia
from django.db.models import Q

User = get_user_model()


# Página inicial
class IndexView(ListView):
    context_object_name = 'noticias_home_page'
    #queryset = Noticia.objects.filter(~Q(image='')).order_by('-published_at')[0:3]
    queryset = Noticia.objects.all().order_by('-published_at')[0:3]
    template_name = 'index.html'


# Página sobre o projeto
class AboutView(TemplateView):
    template_name = 'about.html'


# Página de parceiros
class PartnersView(TemplateView):
    template_name = 'partners.html'


# Página de dúvidas
class FaqView(TemplateView):
    template_name = 'faq.html'


# Página do conselho executivo
class ConselhoExecutivoView(TemplateView):
    template_name = 'conselho_executivo.html'


# Página do manual da marca
class ManualMarcaView(TemplateView):
    template_name = 'manual_marca.html'


# Página de contatos
def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulário inválido')
    context = {
        'form': form,
        'success': success,
    }
    return render(request, 'contact.html', context)


index = IndexView.as_view()
about = AboutView.as_view()
partners = PartnersView.as_view()
duvida = FaqView.as_view()
conselho_executivo = ConselhoExecutivoView.as_view()
manual_marca = ManualMarcaView.as_view()
