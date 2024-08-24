from django.urls import path
from . import views
from .views import bienvenida_view, siguiente_view


urlpatterns = [
    path('bienvenida/', bienvenida_view, name='bienvenida'),
    path('siguiente/', views.graph_view, name='siguiente'),
    path('', views.home_view, name='home_view'),
    
]
