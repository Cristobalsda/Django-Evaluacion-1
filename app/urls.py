from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuario/', views.usuarios, name='usuarios'),
    path('juguetes/', views.juguetes, name='juguetes'),
    path('ropa/', views.ropa, name='ropa'),
    path('categorias/', views.categorias, name='categoria'),
    path('electronica/', views.electronica, name='electronica'),
]
