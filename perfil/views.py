from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import UsuarioForm
from django.contrib.auth import login

def home(request):
    group = request.user.groups.values_list('name', flat=True).first()
    return render(request, 'home.html', {'group': group})

class UsuarioCreate(CreateView):
    template_name = "cadastro.html"
    form_class = UsuarioForm

    def form_valid(self, form):
        username = form.cleaned_data['username']  # Supondo que o campo de nome no formulário seja 'nome'
        if len(username) < 6 or len(username) > 15:
            form.add_error('username', 'O nome deve ter entre 6 e 15 caracteres')
            return self.form_invalid(form)
        
        user = form.save()
        
        # Autentique o usuário após o registro
        login(self.request, user)
        
        # Redirecione para a página inicial ou outra página desejada
        return redirect('home')

def meu_perfil(request):
    group = request.user.groups.values_list('name', flat=True).first()
    user = request.user
    password = len(user.password)
    return render(request, 'meu_perfil.html', {'password': password, 'group': group})