from django.urls import path
from . import views
from .views import ShowCreate

urlpatterns = [
    path('exibir_shows', views.exibir_shows, name='exibir_shows'),
    path('cadastrar_shows', ShowCreate.as_view(), name='cadastrar_shows'),
]