from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

#Todas las categorias.
class HerramientaManualForm(forms.ModelForm):
    class Meta:
        model = HerramientaManual
        fields = [
            "nombre",
            "cantidad",
            "ubicacion",
            "partida",
        ]

class MaterialFerreteriaForm(forms.ModelForm):
    class Meta:
        model = HerramientaManual
        fields = [
            "nombre",
            "cantidad",
            "ubicacion",
            "partida",
        ]

class MaterialLimpiezaForm(forms.ModelForm):
    class Meta:
        model = HerramientaManual
        fields = [
            "nombre",
            "cantidad",
            "ubicacion",
            "partida",
        ]

class EquipoMantenimientoForm(forms.ModelForm):
    class Meta:
        model = HerramientaManual
        fields = [
            "nombre",
            "cantidad",
            "ubicacion",
            "partida",
        ]

class EquipoJardineriaForm(forms.ModelForm):
    class Meta:
        model = HerramientaManual
        fields = [
            "nombre",
            "cantidad",
            "ubicacion",
            "partida",
        ]
class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = [
            "content_type",
            "object_id",
            "cantidad_prestada",
            "fecha_termino",
            "plantel_origen",
            "plantel_destino",
            "usuario",
        ]
    object_id = forms.IntegerField(label='ID de la herramienta')
    cantidad_prestada = forms.IntegerField(label='Cantidad prestada')
    fecha_termino = forms.DateField(label='Fecha de término')
    plantel_origen = forms.ChoiceField(choices=[
        ('Unidad Tomas Aquino', 'Unidad Tomas Aquino'),
        ('Unidad Otay', 'Unidad Otay')
    ], label='Plantel de origen')
    plantel_destino = forms.ChoiceField(choices=[
        ('Unidad Tomas Aquino', 'Unidad Tomas Aquino'),
        ('Unidad Otay', 'Unidad Otay')
    ], label='Plantel de destino')
    usuario = forms.ModelChoiceField(queryset=User.objects.all(), label='Usuario')

    def __init__(self, *args, **kwargs):
        super(PrestamoForm, self).__init__(*args, **kwargs)
        
        # Filtra los ContentType para incluir solo los modelos específicos
        allowed_models = [HerramientaManual, MaterialFerreteria, MaterialLimpieza, EquipoJardineria, EquipoMantenimiento]
        
        # Usa `ContentType.objects.get_for_models` para obtener solo los ContentTypes de los modelos deseados
        content_types = ContentType.objects.get_for_models(*allowed_models)
        self.fields['content_type'].queryset = ContentType.objects.filter(id__in=[ct.id for ct in content_types.values()])
        # Especificar el tipo de campo de fecha de vencimiento como 'date'
        self.fields['content_type'].label = "Selecciona el tipo de herramienta"
        self.fields['fecha_termino'].widget = forms.DateInput(attrs={'type': 'date'})
################## UPDATES ###################

class UpdateHerramientaManualForm(forms.ModelForm):
    class Meta:
        model = HerramientaManual
        fields = [
            "cantidad",
            "ubicacion",
        ]

class UpdateMaterialLimpiezaForm(forms.ModelForm):
    class Meta:
        model = MaterialLimpieza
        fields = [
            "cantidad",
            "ubicacion",
        ]
class UpdateMaterialFerreterriaForm(forms.ModelForm):
    class Meta:
        model = MaterialFerreteria
        fields = [
            "cantidad",
            "ubicacion",
        ]

class UpdateEquipoMantenimientoForm(forms.ModelForm):
    class Meta:
        model = EquipoMantenimiento
        fields = [
            "cantidad",
            "ubicacion",
        ]

class UpdateEquipoJardineriaForm(forms.ModelForm):
    class Meta:
        model = EquipoJardineria
        fields = [
            "cantidad",
            "ubicacion",
        ]

class UpdatePrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = [
            "fecha_termino",
            "finalizado",
        ]
        widgets = {
            "fecha_termino": forms.DateInput(attrs={"type": "date", "class": "form-control"}),  # Declaramos el DateInput
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]