"""
URL configuration for venta_tecnologica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from ventas import views

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el administrador de Django
    path('', views.lista_productos, name='home'),  # Redirigir la raíz a la lista de productos
    path('productos/', include('ventas.urls')),  # Incluir las URLs de la aplicación 'ventas'
]