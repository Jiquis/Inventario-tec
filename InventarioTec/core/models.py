from django.db import models
from django.contrib.auth.models import User  # Importa el modelo User
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Modelo base para los items
class Item(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    ubicacion = models.CharField(max_length=100, blank=True, null=True, choices=[('Unidad Tomas Aquino', 'Unidad Tomas Aquino'), ('Unidad Otay', 'Unidad Otay')])
    partida = models.CharField(max_length=5, null=True, blank = True)
    class Meta:
        abstract = True  # Esto hace que no se cree una tabla para el modelo base

# Modelo para Herramientas manuales
class HerramientaManual(Item):
    tipo = models.CharField(max_length=50, default='Herramienta manual')

class MaterialFerreteria(Item):
    tipo = models.CharField(max_length=50, default='Material de ferreteria')

# Modelo para Material de limpieza
class MaterialLimpieza(Item):
    tipo = models.CharField(max_length=50, default='Material de limpieza')

# Modelo para Equipos de mantenimiento
class EquipoMantenimiento(Item):
    tipo = models.CharField(max_length=50, default='Equipo de mantenimiento')

# Modelo para Equipos de jardinería
class EquipoJardineria(Item):
    tipo = models.CharField(max_length=50, default='Equipo de jardineria')

# Modelo de Prestamo
class Prestamo(models.Model):
#   Estos dos campos serán usados por GenericForeignKey para hacer la relación
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    
    # Este es el campo genérico que apunta a cualquier modelo basado en `Item`
    item = GenericForeignKey('content_type', 'object_id')    
    cantidad_prestada = models.IntegerField()  # Cantidad de materiales prestados
    fecha_inicio = models.DateField(default=timezone.now)  # Fecha de inicio del préstamo
    fecha_termino = models.DateField()  # Fecha de término del préstamo
    plantel_origen = models.CharField(max_length=50, choices=[('Unidad Tomas Aquino', 'Unidad Tomas Aquino'), ('Unidad Otay', 'Unidad Otay')])  # Plantel que realiza el préstamo
    plantel_destino = models.CharField(max_length=50, choices=[('Unidad Tomas Aquino', 'Unidad Tomas Aquino'), ('Unidad Otay', 'Unidad Otay')])  # Plantel que recibe el préstamo
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario que recibe el préstamo
    finalizado = models.BooleanField(default=False)  # Indicador de si el préstamo ha finalizado

    def __str__(self):
        return f"{self.item.nombre} - {self.cantidad_prestada} unidades prestadas a {self.usuario.username} desde {self.plantel_origen} hasta {self.plantel_destino}"

    def save(self, *args, **kwargs):
        # Obtener el valor anterior de `finalizado`
        is_new = self.pk is None
        was_finalizado = None

        if not is_new:
            was_finalizado = Prestamo.objects.get(pk=self.pk).finalizado

        # Descontar la cantidad si es un nuevo préstamo y no está finalizado
        if is_new and not self.finalizado:
            if self.cantidad_prestada > self.item.cantidad:
                raise ValueError("La cantidad prestada no puede exceder la cantidad disponible del item.")
            self.item.cantidad -= self.cantidad_prestada
            self.item.save()

        # Devolver cantidad si el préstamo está marcado como finalizado y antes no lo estaba
        if was_finalizado is False and self.finalizado:
            self.item.cantidad += self.cantidad_prestada
            self.item.save()

        super().save(*args, **kwargs)