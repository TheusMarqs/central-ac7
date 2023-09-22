from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Show
from django.urls import reverse_lazy

def exibir_shows(request):
    shows = Show.objects.all()
    return render(request, 'exibir_shows.html', {'shows': shows})

class ShowCreate(CreateView):
    model = Show
    fields = ['artist', 'price', 'description', 'date', 'city', 'neighbourhood', 'street', 'cep', 'image']
    template_name = 'cadastrar_shows.html'
    success_url = reverse_lazy('exibir_shows')

class ShowUpdate(UpdateView):
    model = Show
    fields = ['artist', 'price', 'description', 'date', 'city', 'neighbourhood', 'street', 'cep', 'image']
    template_name = 'cadastrar_shows.html'
    success_url = reverse_lazy('exibir_shows')

class ShowDelete(DeleteView):
    model = Show
    template_name = 'exibir_shows.html'
    success_url = reverse_lazy('exibir_shows')

def ingresso(request, id):
    shows = Show.objects.filter(id=id)
    return render(request, 'ingresso.html', {'shows': shows})