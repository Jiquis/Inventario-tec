from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
class Index(generic.View):
    template_name = "core/index.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
            "HerramientaManual": HerramientaManual.objects.all(),
            "MaterialFerreteria": MaterialFerreteria.objects.all(),
            "MaterialLimpieza": MaterialLimpieza.objects.all(),
            "EquipoMantenimiento" : EquipoMantenimiento.objects.all(),
            "EquipoJardineria" : EquipoJardineria.objects.all() 
        }
        return render(request, self.template_name, self.context)
class Prestamos(generic.View):
    template_name = "core/prestamos.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
            "PrestamosR": Prestamo.objects.all(),
        }
        return render(request, self.template_name, self.context)

##################### FULL CALENDAR ############################### 
class FullCalendarGG(generic.View):
    template_name = "fullcalendar/fullcalendar.html"
    context = {}

    def get(self, request):
        self.context = {
            "PrestamosR": Prestamo.objects.filter(finalizado=False)
        }
        return render(request, self.template_name, self.context)
    
################## HERRAMIENTAS EN LISTA #######################
class ListHerramientaManual(generic.View):
    template_name = "core/Catalogo1.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
        "HerramientaManual": HerramientaManual.objects.all(),
        }
        return render(request, self.template_name, self.context)

class ListMaterialFerreteria(generic.View):
    template_name = "core/Catalogo2.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
        "MaterialFerreteria": MaterialFerreteria.objects.all(),
        }
        return render(request, self.template_name, self.context)

class ListMaterialLimpieza(generic.View):
    template_name = "core/Catalogo3.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
        "MaterialLimpieza": MaterialLimpieza.objects.all(),
        }
        return render(request, self.template_name, self.context)
    
class ListEquipoMantenimiento(generic.View):
    template_name = "core/Catalogo4.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
        "EquipoMantenimiento" : EquipoMantenimiento.objects.all(),
        }
        return render(request, self.template_name, self.context)
    
class ListEquipoJardineria(generic.View):
    template_name = "core/Catalogo5.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
        "EquipoJardineria" : EquipoJardineria.objects.all(), 
        }
        return render(request, self.template_name, self.context)
    
################## DETALLES PRESTAMO #############################
    
class DetailPrestamos(generic.DetailView):
    template_name = "core/detalles_prestamos.html"
    model = Prestamo

################## ACTUALIZAR PRESTAMO ############################
class UpdatePrestamos(generic.UpdateView):
    template_name = "core/actualizar_prestamo.html"
    model = Prestamo
    form_class = UpdatePrestamoForm
    success_url = reverse_lazy("prestamos")

################# NUEVO PRESTAMO ################################
class NewPrestamos(generic.CreateView):
    template_name = "core/nuevo_prestamo.html"
    model = Prestamo
    form_class = PrestamoForm
    success_url = reverse_lazy("prestamos")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Agrupar las herramientas por tipo
        context['herramientas_herramientamanual'] = list(HerramientaManual.objects.values('id', 'nombre'))
        context['herramientas_materiallimpieza'] = list(MaterialLimpieza.objects.values('id', 'nombre'))
        context['herramientas_materialferreteria'] = list(MaterialFerreteria.objects.values('id', 'nombre'))
        context['herramientas_equipomantenimiento'] = list(EquipoMantenimiento.objects.values('id', 'nombre'))
        context['herramientas_equipojardineria'] = list(EquipoJardineria.objects.values('id', 'nombre'))
        return context
    
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_todos')  # Redirigir al login después del registro
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/registrar.html', {'form': form})

def register1(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigir al login después del registro
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/registrar2.html', {'form': form})

################## EDITAR INVENTARIO ###########################
class UpdateHerramientaManual(generic.UpdateView):
    template_name = "updates/actualizar_inventario1.html"
    model = HerramientaManual
    form_class = UpdateHerramientaManualForm
    success_url = reverse_lazy("catalogo 1")

class UpdateMaterialFerreteria(generic.UpdateView):
    template_name = "updates/actualizar_inventario2.html"
    model = MaterialFerreteria
    form_class = UpdateMaterialFerreterriaForm
    success_url = reverse_lazy("catalogo 2")

class UpdateMaterialLimpieza(generic.UpdateView):
    template_name = "updates/actualizar_inventario3.html"
    model = MaterialLimpieza
    form_class = UpdateMaterialLimpiezaForm
    success_url = reverse_lazy("catalogo 3")

class UpdateEquipoMantenimiento(generic.UpdateView):
    template_name = "updates/actualizar_inventario4.html"
    model = EquipoMantenimiento
    form_class = UpdateEquipoMantenimientoForm
    success_url = reverse_lazy("catalogo 4")

class UpdateEquipoJardineria(generic.UpdateView):
    template_name = "updates/actualizar_inventario5.html"
    model = EquipoJardineria
    form_class = UpdateEquipoJardineriaForm
    success_url = reverse_lazy("catalogo 5")

################# CREAR INVENTARIO ##########################
class NewHerramientaManual(generic.CreateView):
    template_name = "create/crear_1.html"
    model = HerramientaManual
    form_class = HerramientaManualForm
    success_url = reverse_lazy("catalogo 1")

class NewMaterialFerreteria(generic.CreateView):
    template_name = "create/crear_2.html"
    model = MaterialFerreteria
    form_class = MaterialFerreteriaForm
    success_url = reverse_lazy("catalogo 2")

class NewMaterialLimpieza(generic.CreateView):
    template_name = "create/crear_3.html"
    model = MaterialLimpieza
    form_class = MaterialLimpiezaForm
    success_url = reverse_lazy("catalogo 3")

class NewEquipoMantenimiento(generic.CreateView):
    template_name = "create/crear_4.html"
    model = EquipoMantenimiento
    form_class = EquipoMantenimientoForm
    success_url = reverse_lazy("catalogo 4")

class NewEquipoJardineria(generic.CreateView):
    template_name = "create/crear_5.html"
    model = EquipoJardineria
    form_class = EquipoJardineriaForm
    success_url = reverse_lazy("catalogo 5")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Verificar si pertenece a los grupos
            if user.groups.filter(name='Jefe de departamento').exists():
                return redirect('prestamos')
            elif user.groups.filter(name='Manejo de prestamos').exists():
                return redirect('prestamos')
            else:
                return HttpResponse("No tienes permiso para acceder al sistema.")
        else:
            return render(request, 'core/login.html', {'error': 'Usuario o contraseña incorrectos.'})
    
    return render(request, 'core/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirige al login después de cerrar sesión

@login_required
def jefes_dashboard(request):
    return HttpResponse("""
        Bienvenido al Panel de Jefes (En construcción)
        <br>
        <a href='/logout/'>Cerrar Sesión</a>
    """)

@login_required
def gestores_dashboard(request):
    return HttpResponse("""
        Bienvenido al Panel de Gestores (En construcción)
        <br>
        <a href='/logout/'>Cerrar Sesión</a>
    """)