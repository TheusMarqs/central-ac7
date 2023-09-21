from django.db import models
import os

class Show(models.Model):
    artist = models.CharField(max_length=25, verbose_name='Nome do artista')
    value = models.FloatField(verbose_name='Valor do ingresso')
    date = models.DateField(verbose_name='Data do show')
    description = models.TextField(verbose_name='Descrição do show')
    image = models.ImageField(verbose_name='Imagem de capa', upload_to="img")

    def delete(self, *args, **kwargs):
        # Antes de excluir o objeto, exclua também a imagem associada
        self.image.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.artist