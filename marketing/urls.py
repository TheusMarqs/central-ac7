from django.urls import path
from . import views

urlpatterns = [
    path('publicidade', views.publicidade, name="publicidade"),
]
