from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('cadastro/', UsuarioCreate.as_view(), name='cadastro'),
]