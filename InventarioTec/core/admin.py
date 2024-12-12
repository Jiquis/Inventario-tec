from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(HerramientaManual)
class HerramientaManualAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cantidad', 'ubicacion', 'id', 'partida']

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['item', 'cantidad_prestada', 'fecha_inicio', 'fecha_termino', 'plantel_origen', 'plantel_destino']

@admin.register(MaterialLimpieza)
class MaterialLimpiezaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cantidad', 'ubicacion', 'id', 'partida']

@admin.register(MaterialFerreteria)
class MaterialFerreteriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cantidad', 'ubicacion', 'id', 'partida']

@admin.register(EquipoMantenimiento)
class EquipoMantenimientoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cantidad', 'ubicacion', 'id', 'partida']

@admin.register(EquipoJardineria)
class EquipoJardineriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cantidad', 'ubicacion', 'id', 'partida']
