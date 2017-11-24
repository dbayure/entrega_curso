from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.http import HttpResponse
from .forms import PrestamoForm, LibroForm, DevolucionForm, SocioForm, AutorForm, Autor_LibroForm

from .models import Libro, Copia, Socio, Prestamo, Devolucion, Autor, Autores_Libros

def index(request):
    return render(request, 'biblio/index.html')

def libros(request):
    libros = Libro.objects.order_by('-titulo')[:5]
    context = {'libros' : libros}
    return render(request, 'biblio/libros.html', context)

def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    return render(request, 'biblio/detalle_libro.html', {'libro': libro})

def libro_nuevo(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save()
    form = LibroForm()
    return render(request, 'biblio/libro_nuevo.html', {'form': form})

def prestamos(request):
    prestamos = Prestamo.objects.order_by('-id')
    context = {'prestamos': prestamos}
    return render(request, 'biblio/prestamos.html', context)

def detalle_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, pk=prestamo_id)
    return render(request, 'biblio/detalle_prestamo.html', {'prestamo': prestamo})

def prestamo_nuevo(request):
    if request.method == "POST":
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save()
            return prestamos(request)
    else:
        form = PrestamoForm()
    return render(request, 'biblio/prestamo_nuevo.html', {'form': form})
   
def devoluciones (request):
    total_devoluciones = Devolucion.objects.order_by('-id')[:5]
    context = {'lista_devoluciones' : total_devoluciones}
    return render(request, 'biblio/devoluciones.html', context)

def detalle_devolucion (request, devolucion_id):
    devolucion = get_object_or_404(Devolucion, pk=devolucion_id)
    return render(request, 'biblio/detalle_devolucion.html', {'devolucion': devolucion})
   
def devolucion_nueva(request):
    if request.method == "POST":
        form = DevolucionForm(request.POST)
        if form.is_valid():
            devolucion = form.save()
            return devoluciones(request)
    else:
        form = DevolucionForm()
    return render(request, 'biblio/devolucion_nueva.html', {'form': form})

def activos (request):
    activos = Socio.objects.order_by('-id')[:5]
    context = {'activos' : activos}
    return render(request, 'biblio/activos.html', context)

def morosos (request):
    morosos = Socio.objects.order_by('-id')[:5]
    context = {'morosos' : morosos}
    return render(request, 'biblio/morosos.html', context)
   
def futuros_morosos (request):
    futuros_morosos = Socio.objects.order_by('-id')[:5]
    context = {'futuros_morosos' : futuros_morosos}
    return render(request, 'biblio/futuros_morosos.html', context)
   
def detalle_socio (request,socio_id):
    socio = get_object_or_404(Socio, pk=socio_id)
    return render(request, 'biblio/detalle_socio.html', {'socio': socio})
   
def detalle_copia (request):
    pass
   
def socios(request):
    socios = Socio.objects.order_by('-id')[:5]
    context = {'socios' : socios}
    return render(request, 'biblio/socios.html', context)

def detalle_socio(request, socio_id):
    socio = get_object_or_404(Socio, pk=socio_id)
    return render(request, 'biblio/detalle_socio.html', {'socio': socio})

def socio_nuevo(request):
    if request.method == "POST":
        form = SocioForm(request.POST)
        if form.is_valid():
            socio = form.save()
    form = SocioForm()
    return render(request, 'biblio/socio_nuevo.html', {'form': form})

def autores(request):
    autores = Autor.objects.order_by('-id')
    context = {'autores' : autores}
    return render(request, 'biblio/autores.html', context)

def detalle_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    return render(request, 'biblio/detalle_autor.html', {'autor': autor})

def autor_nuevo(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = form.save()
    form = AutorForm()
    return render(request, 'biblio/autor_nuevo.html', {'form': form})

def autores_libros(request):
    autores = Autor.objects.order_by('-id')
    libros = Libro.objects.order_by('-id')
    al = Autores_Libros.objects.order_by('-autores')
    context = {'autores' : autores, 'libros' : libros, 'al': al}
    return render(request, 'biblio/autores_libros.html', context)

def autores_libros_nuevo(request, autor_id, libro_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    libro = get_object_or_404(Libro, pk=libro_id)
    al = Autores_Libros()
    al.autores.add(autor)
    al.libros.add(libro)
    al.save()
    return render(request, 'biblio/autores_libros.html', context)


