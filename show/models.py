from django.db import models
import os
from django.utils import timezone
from django.core.exceptions import ValidationError

class Show(models.Model):
    choice_city = (
        ('Itu', 'Itu'),
        ('Salto', 'Salto'),
        ('Campinas', 'Campinas')
    )

    artist = models.CharField(max_length=25, verbose_name='Nome do artista')
    price = models.FloatField(verbose_name='Valor do ingresso')
    datetime = models.DateTimeField(verbose_name='Data e horário do show')
    description = models.TextField(verbose_name='Descrição do show')
    image = models.ImageField(verbose_name='Imagem de capa', upload_to="img")
    city = models.CharField(verbose_name='Cidade', choices=choice_city, max_length=15)
    neighbourhood = models.CharField(verbose_name='Bairro', max_length=25, null=True, blank=True)
    street = models.CharField(verbose_name='Rua', max_length=50, null=True, blank=True)
    cep = models.CharField(max_length=10, null=True, blank=True)

    def clean(self):
        current_datetime = timezone.localtime(timezone.now())
        current_hour = current_datetime.time().hour

        if self.datetime.date() < current_datetime.date() or (self.datetime.date() == current_datetime.date() and self.datetime.time().hour < current_hour):
            raise ValidationError('A data e hora do show não pode ser no passado.')

    def delete(self, *args, **kwargs):
        # Antes de excluir o objeto, exclua também a imagem associada
        self.image.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.artist