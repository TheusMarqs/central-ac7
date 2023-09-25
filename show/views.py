from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Show
from django.urls import reverse_lazy
from .forms import ShowForm
import mercadopago
from core import settings

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
    

    sdk = mercadopago.SDK("TEST-6540474833878444-092507-74467a0e593855cfde4d00bb2d3b0c4b-1218207994")


    payment_data = {
        "transaction_amount": float(request.POST.get("transaction_amount")),
        "token": request.POST.get("token"),
        "description": request.POST.get("description"),
        "installments": int(request.POST.get("installments")),
        "payment_method_id": request.POST.get("payment_method_id"),
        "notification_url": "http://requestbin.fullcontact.com/1ogudgk1",
        "payer": {
            "email": request.POST.get("email"),
            "identification": {
                "type": request.POST.get("type"), 
                "number": request.POST.get("number")
            }
        }
    }

    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]


    print(payment)

    return render(request, 'ingresso.html', {'shows': shows, 'artist': artist})

def filtrar_shows(request, city):
    shows = Show.objects.filter(city__icontains=city)
    return render(request, 'exibir_shows.html', {'shows':shows})
