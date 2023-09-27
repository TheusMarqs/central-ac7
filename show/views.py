from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Show
from django.urls import reverse_lazy
from .forms import ShowForm
import mercadopago
from braces.views import GroupRequiredMixin
from django.contrib.messages import constants
from django.contrib import messages


def exibir_shows(request):
    group = request.user.groups.values_list('name', flat=True).first()
    shows = Show.objects.all()
    return render(request, 'exibir_shows.html', {'shows': shows, 'group': group})

class ShowCreate(GroupRequiredMixin, CreateView):
    group_required = u"admin"
    model = Show
    form_class = ShowForm
    template_name = 'cadastrar_shows.html'
    success_url = reverse_lazy('exibir_shows')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, constants.SUCCESS, 'Show cadastrado com sucesso!')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        txtBtn = 'Cadastrar'
        context["txtBtn"] = txtBtn
        return context
    


class ShowUpdate(GroupRequiredMixin, UpdateView):
    group_required = u"admin"
    model = Show
    form_class = ShowForm
    template_name = 'cadastrar_shows.html'
    success_url = reverse_lazy('exibir_shows')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, constants.SUCCESS, 'Show atualizado com sucesso!')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        txtBtn = 'Atualizar'
        context["txtBtn"] = txtBtn
        return context

class ShowDelete(GroupRequiredMixin, DeleteView):
    group_required = u"admin"
    model = Show
    template_name = 'exibir_shows.html'
    success_url = reverse_lazy('exibir_shows')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, constants.SUCCESS, 'Show excluído com sucesso!')
        return response

def ingresso(request, id):
    group = request.user.groups.values_list('name', flat=True).first()
    shows = Show.objects.filter(id=id)
    for show in shows:
        artist = show.artist
    
    """
    sdk = mercadopago.SDK("TEST-67bae85d-2d4d-4843-8483-beb6dc42385a")


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
    """

    return render(request, 'ingresso.html', {'shows': shows, 'artist': artist, 'group': group})

def filtrar_shows(request, city):
    group = request.user.groups.values_list('name', flat=True).first()
    shows = Show.objects.filter(city__icontains=city)
    return render(request, 'exibir_shows.html', {'shows':shows, 'group':group})
