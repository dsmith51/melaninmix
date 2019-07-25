from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView

from .models import Bio, About, HomePage


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(ListView):
    model = About
    context_object_name = 'information'
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


def bios_list(request):
    bios = Bio.objects.all()
    context = {'bios': bios}
    return render(request, 'bio.html', context)


def about(request):
    information = About.objects.all()
    context = {'information': information}
    return render(request, 'about.html', context)


def home_page_view(request):
    content = HomePage.objects.all()
    context = {'content': content}
    return render(request, 'home.html', context)
