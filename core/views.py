# coding=utf-8
from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.generic import View, TemplateView, ListView
from content.models import Noticia, Timeline
from django.db.models import Q
from django.shortcuts import render_to_response
from django.template import RequestContext

User = get_user_model()


# Página inicial
class IndexView(ListView):
    context_object_name = 'noticias_home_page'
    queryset = Noticia.objects.filter(~Q(image='')).order_by('-published_at')[0:3]
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['timeline_itens'] = Timeline.objects.all()
        return context


# Página sobre o projeto
class AboutView(TemplateView):
    template_name = 'about.html'


# Página de parceiros
class PartnersView(TemplateView):
    template_name = 'partners.html'

# Página do manual da marca
class ManualMarcaView(TemplateView):
    template_name = 'manual_marca.html'


# Página Plano de Providencias
class PlanoProvidenciaView(TemplateView):
    template_name = 'plano_providencias.html'


# Página Criterios e regras
class CriteriosRegrasView(TemplateView):
    template_name = 'criterios_regras.html'


# Página Criterios e regras
class AcervoView(TemplateView):
    template_name = 'acervo.html'


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


# HTTP Error 404
def page_not_found(request):
    return render(request, '404.html')


def server_error(request):
    return render(request,  '500.html')


index = IndexView.as_view()
about = AboutView.as_view()
partners = PartnersView.as_view()
manual_marca = ManualMarcaView.as_view()
plano_providencias = PlanoProvidenciaView.as_view()
criterios_regras = CriteriosRegrasView.as_view()
acervo = AcervoView.as_view()
