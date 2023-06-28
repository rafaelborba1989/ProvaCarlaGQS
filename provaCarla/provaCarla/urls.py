"""
URL configuration for provaCarla project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
path('coletas/', views.listar_coletas, name='listar_coletas'),
    path('coletas/<int:coleta_id>/', views.detalhes_coleta, name='detalhes_coleta'),
    path('coletas/<int:coleta_id>/deletar/', views.deletar_coleta, name='deletar_coleta'),
    path('coletas/criar/', views.criar_coleta, name='criar_coleta'),
    path('criacao/criar/', views.criar_criacao, name='criar_criacao'),
]


