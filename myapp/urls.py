from django.urls import path
from . import views
from .views import bienvenida_view, siguiente_view


urlpatterns = [
    path('bienvenida/', bienvenida_view, name='bienvenida'),
    path('siguiente/', views.siguiente_view, name='siguiente'),
    path('', views.bienvenida_view, name='bienvenida'),
    
]
