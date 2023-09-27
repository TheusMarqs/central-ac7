from django import forms
from .models import Show

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ['artist', 'price', 'description', 'datetime', 'city', 'neighbourhood', 'street', 'cep', 'image']
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }