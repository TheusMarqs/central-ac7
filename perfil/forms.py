from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Adicione autocomplete="off" aos campos de entrada
        self.fields['username'].widget.attrs.update({'autocomplete': 'off'})
        self.fields['email'].widget.attrs.update({'autocomplete': 'off'})