from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import UsuarioForm
from django.contrib.auth import login

def home(request):
    return render(request, 'home.html')

class UsuarioCreate(CreateView):
    template_name = "cadastro.html"
    form_class = UsuarioForm

    def form_valid(self, form):
        username = form.cleaned_data['username']  # Supondo que o campo de nome no formulário seja 'nome'
        if len(username) < 6:
            form.add_error('username', 'O nome deve ter pelo menos 6 caracteres.')
            return self.form_invalid(form)
        
        user = form.save()
        
        # Autentique o usuário após o registro
        login(self.request, user)
        
        # Redirecione para a página inicial ou outra página desejada
        return redirect('home')

def meu_perfil(request):
    user = request.user
    password = len(user.password)
    return render(request, 'meu_perfil.html', {'password': password})