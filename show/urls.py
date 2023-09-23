from django.urls import path
from . import views
from .views import ShowCreate, ShowUpdate, ShowDelete

urlpatterns = [
    path('exibir_shows', views.exibir_shows, name='exibir_shows'),
    path('cadastrar_shows', ShowCreate.as_view(), name='cadastrar_shows'),
    path('update_show/<int:pk>', ShowUpdate.as_view(), name='update_show'),
    path('delete_show/<int:pk>', ShowDelete.as_view(), name='delete_show'),
    path('ingresso/<int:id>', views.ingresso, name='ingresso'),
    path('filtrar_shows/<str:city>', views.filtrar_shows, name='filtrar_shows'),
]