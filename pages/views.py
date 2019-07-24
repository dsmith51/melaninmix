from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView

from .models import Bio, Episode, About, HomePage


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(ListView):
    model = About
    context_object_name = 'information'
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class BioView(ListView):
    model = Bio
    context_object_name = 'bios'
    template_name = 'bio.html'


class EpisodeView(ListView):
    model = Episode

    template_name = 'episode.html'


def bios_list(request):
    bios = Bio.objects.all()
    context = {'bios': bios}
    return render(request, 'bio.html', context)


def about(request):
    information = About.objects.all()
    context = {'information': information}
    return render(request, 'about.html', context)


def episodes(request):
    eps = Episode.objects.all()
    context = {'episodes': eps}
    return render(request, 'episode.html', context)


def background_pic(request):
    pic = HomePage.picture
    context = {'pic': pic}
    return render(request, 'base.html', context)
