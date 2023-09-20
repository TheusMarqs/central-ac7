# Generated by Django 4.2.5 on 2023-09-20 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=25, verbose_name='Nome do artista')),
                ('value', models.FloatField(verbose_name='Valor do ingresso')),
                ('date', models.DateField(verbose_name='Data do show')),
                ('description', models.TextField(verbose_name='Descrição do show')),
                ('image', models.ImageField(upload_to='img', verbose_name='Imagem de capa')),
            ],
        ),
    ]
