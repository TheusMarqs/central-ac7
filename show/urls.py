from django.urls import path
from . import views
from .views import ShowCreate, ShowUpdate

urlpatterns = [
    path('exibir_shows', views.exibir_shows, name='exibir_shows'),
    path('cadastrar_shows', ShowCreate.as_view(), name='cadastrar_shows'),
    path('update_show/<int:pk>', ShowUpdate.as_view(), name='update_show')
]