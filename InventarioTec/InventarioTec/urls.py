"""
URL configuration for InventarioTec project.

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
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #CATALOGOS GENERAL Y ESPECIFICOS
    path('Catalogo/todo', Index.as_view(), name="lista_todos"),
    path('Catalogo 1/', ListHerramientaManual.as_view(), name="catalogo 1"),
    path('Catalogo 2/', ListMaterialFerreteria.as_view(), name="catalogo 2"),
    path('Catalogo 3/', ListMaterialLimpieza.as_view(), name="catalogo 3"),
    path('Catalogo 4/', ListEquipoMantenimiento.as_view(), name="catalogo 4"),
    path('Catalogo 5/', ListEquipoJardineria.as_view(), name="catalogo 5"),
    #ACTUALIZAR INVENTARIO
    path('actualizar/inventario/herramienta/manual/<int:pk>/', UpdateHerramientaManual.as_view(), name='actualizar inventario 1'),
    path('actualizar/inventario/material/ferreteria/<int:pk>/', UpdateMaterialFerreteria.as_view(), name='actualizar inventario 2'),
    path('actualizar/inventario/material/limpieza/<int:pk>/', UpdateMaterialLimpieza.as_view(), name='actualizar inventario 3'),
    path('actualizar/inventario/equipo/mantenimiento/<int:pk>/', UpdateEquipoMantenimiento.as_view(), name='actualizar inventario 4'),
    path('actualizar/inventario/equipo/jardineria/<int:pk>/', UpdateEquipoJardineria.as_view(), name='actualizar inventario 5'),
    #CREAR INVENTARIO
    path('crear/inventario/herramienta/manual/', NewHerramientaManual.as_view(), name='crear inventario 1'),
    path('crear/inventario/material/ferreteria/', NewMaterialFerreteria.as_view(), name='crear inventario 2'),
    path('crear/inventario/material/limpieza/', NewMaterialLimpieza.as_view(), name='crear inventario 3'),
    path('crear/inventario/equipo/mantenimiento/', NewEquipoMantenimiento.as_view(), name='crear inventario 4'),
    path('crear/inventario/equipo/jardineria/', NewEquipoJardineria.as_view(), name='crear inventario 5'),
    #PRESTAMOS Y DERIVADOS
    path('prestamos/', Prestamos.as_view(), name="prestamos"),
    path('detalles/prestamos/<int:pk>/', DetailPrestamos.as_view(), name="detalles de prestamo"),
    path('actualizar/prestamo/<int:pk>/', UpdatePrestamos.as_view(), name="actualizar prestamo"),
    path('nuevo/prestamo/', NewPrestamos.as_view(), name="nuevo prestamo"),
    path('calendario/prestamo/', FullCalendarGG.as_view(), name="calendario"),
    #USUARIOS
    path('registro/', register, name='registro'),
    path('registro1/', register1, name='registro1'),
    path('', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
