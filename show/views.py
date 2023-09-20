from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Show
from django.urls import reverse_lazy

def exibir_shows(request):
    shows = Show.objects.all()
    return render(request, 'exibir_shows.html', {'shows': shows})

class ShowCreate(CreateView):
    model = Show
    fields = ['artist', 'value', 'description', 'date', 'image']
    template_name = 'cadastrar_shows.html'
    success_url = reverse_lazy('exibir_shows')