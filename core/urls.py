from django.contrib import admin
from django.urls import path, include
from perfil import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('perfil/', include('perfil.urls')),
    path('podcast/', include('podcast.urls')),
    path('show/', include('show.urls')),
]
