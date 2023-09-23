from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import UsuarioForm
from django.contrib.auth import login

def home(request):
    return render(request, 'home.html')

class UsuarioCreate(CreateView):
    template_name = "cadastro.html"
    form_class = UsuarioForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Autentique o usuário após o registro
            login(request, user)
            
            # Redirecione para a página inicial ou outra página desejada
            return redirect('home')
        return render(request, self.template_name, {'form': form})