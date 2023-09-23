from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Show
from django.urls import reverse_lazy
from .forms import ShowForm
from django.utils import timezone
import datetime

def exibir_shows(request):
    shows = Show.objects.all()
    return render(request, 'exibir_shows.html', {'shows': shows})

class ShowCreate(CreateView):
    model = Show
    form_class = ShowForm
    template_name = 'cadastrar_shows.html'
    success_url = reverse_lazy('exibir_shows')


class ShowUpdate(UpdateView):
    model = Show
    form_class = ShowForm
    template_name = 'cadastrar_shows.html'
    success_url = reverse_lazy('exibir_shows')

class ShowDelete(DeleteView):
    model = Show
    template_name = 'exibir_shows.html'
    success_url = reverse_lazy('exibir_shows')

def ingresso(request, id):
    shows = Show.objects.filter(id=id)
    for show in shows:
        artist = show.artist
    return render(request, 'ingresso.html', {'shows': shows, 'artist': artist})

def filtrar_shows(request, city):
    shows = Show.objects.filter(city__icontains=city)
    return render(request, 'exibir_shows.html', {'shows':shows})