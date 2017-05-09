# coding=utf-8
from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.generic import View, TemplateView

User = get_user_model()


# Página inicial
class IndexView(TemplateView):
    template_name = 'index.html'


# Página sobre o projeto
class AboutView(TemplateView):
    template_name = 'about.html'


# Página de parceiros
class PartnersView(TemplateView):
    template_name = 'partners.html'


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