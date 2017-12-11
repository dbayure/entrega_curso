from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.http import HttpResponse
from .forms import PrestamoForm, PrestamoIdForm, LibroForm, DevolucionForm, SocioForm, AutorForm, PickAutorForm, CopiaForm
from datetime import datetime, date, time, timedelta

from .models import Libro, Copia, Socio, Prestamo, Devolucion, Autor
from .extras import puedo_prestar, socio_moroso, futuro_moroso

def index(request):
    return render(request, 'biblio/index.html')

def libros(request):
    libros = Libro.objects.order_by('-titulo')[:5]
    context = {'libros' : libros}
    return render(request, 'biblio/libros.html', context)

def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    form = PickAutorForm()
    context = {'form' : form, 'libro': libro}
    return render(request, 'biblio/detalle_libro.html', context)

def libro_nuevo(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save()
            libro.save()
    form = LibroForm()
    return render(request, 'biblio/libro_nuevo.html', {'form': form})

def prestamos(request):
    prestamos = Prestamo.objects.order_by('-id')
    context = {'prestamos': prestamos}
    return render(request, 'biblio/prestamos.html', context)

def detalle_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, pk=prestamo_id)
    return render(request, 'biblio/detalle_prestamo.html', {'prestamo': prestamo})

def prestamo_nuevo(request, copia_id=0):
    mensaje = ""
    print ("valore del id de la copia que viene {}".format(copia_id))
    if copia_id == 0:
        if request.method == "POST":
            form = PrestamoForm(request.POST)
            if form.is_valid():
                socio = form.cleaned_data['socio']
                copia = form.cleaned_data['copia']
                if puedo_prestar(socio, copia):
                    prestamo = form.save()
                    copia.estado=True
                    copia.save()
                    mensaje = "Prestamo realizado correctamente"
                else:
                    mensaje = "Erro al realizar el prestamo, no existen copias disponibles o el usuario esta moroso"
        form = PrestamoForm()
        context = {'msg' : mensaje, 'form': form}     
        return render(request, 'biblio/prestamo_nuevo.html', context)
    else: 
        copia = get_object_or_404(Copia, pk=copia_id)
        if request.method == "POST":
            form = PrestamoIdForm(request.POST)
            if form.is_valid():
                socio = form.cleaned_data['socio']
                if puedo_prestar(socio, copia):
                    prestamo = form.save(commit=False)
                    prestamo.copia=copia
                    prestamo.save()
                    copia.estado=True
                    copia.save()
                    mensaje = "Prestamo realizado correctamente"
                else:
                    mensaje = "Erro al realizar el prestamo, no existen copias disponibles o el usuario esta moroso"
        form = PrestamoIdForm()   
        context = {'msg' : mensaje, 'form': form}     
        return render(request, 'biblio/prestamo_nuevo.html', context)
   
def devoluciones (request):
    devoluciones = Devolucion.objects.order_by('-id')
    context = {'devoluciones' : devoluciones}
    return render(request, 'biblio/devoluciones.html', context)

def detalle_devolucion (request, devolucion_id):
    devolucion = get_object_or_404(Devolucion, pk=devolucion_id)
    return render(request, 'biblio/detalle_devolucion.html', {'devolucion': devolucion})
   
def devolucion_nueva(request, prestamo_id=0):
    if prestamo_id == 0:
        if request.method == "POST":
            form = DevolucionForm(request.POST)
            if form.is_valid():
                devolucion = form.save(commit=False)    
                socio_moroso(devolucion.socio, devolucion.copia, form.cleaned_data['fecha_devolucion'])
                devolucion.save()
    else:
        devolucion = Devolucion()
        fecha_devolucion = date.today()
        prestamo = get_object_or_404(Prestamo, pk=prestamo_id)
        copia = get_object_or_404(Copia, pk=prestamo.copia.id)
        socio = get_object_or_404(Socio, pk=prestamo.socio.id)
        devolucion.copia = copia
        devolucion.socio = socio
        devolucion.estado = True
        devolucion.fecha_devolucion = fecha_devolucion
        devolucion.save()
        copia.estado = False
        copia.save()
        prestamo.estado = True
        prestamo.save()
        socio_moroso(socio,copia, fecha_devolucion)
    devoluciones = Devolucion.objects.order_by('-id')
    context = {'devoluciones' : devoluciones}
    return render(request, 'biblio/devoluciones.html', context)

def activos (request):
    activos = Socio.objects.order_by('-id')
    context = {'activos' : activos}
    return render(request, 'biblio/activos.html', context)

def morosos (request):
    morosos = Socio.objects.all().filter(estado=True)
    context = {'morosos' : morosos}
    return render(request, 'biblio/morosos.html', context)
   
def futuros_morosos (request):
    socios = Socio.objects.order_by('-id')
    morosos = futuro_moroso(socios)
    context = {'futuros_morosos' : morosos}
    return render(request, 'biblio/futuros_morosos.html', context)
   
def detalle_socio (request,socio_id):
    socio = get_object_or_404(Socio, pk=socio_id)
    return render(request, 'biblio/detalle_socio.html', {'socio': socio})
   
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

def copias (request):
    copias = Copia.objects.order_by('-id')
    context = {'copias' : copias}
    return render(request, 'biblio/copias.html', context)

def detalle_copia (request, copia_id):
    copia = get_object_or_404(Copia, pk=copia_id)
    return render(request, 'biblio/detalle_copia.html', {'copia': copia})
   
def copia_nueva(request):
    if request.method == "POST":
        form = CopiaForm(request.POST)
        if form.is_valid():
            copia = form.save()
    form = CopiaForm()
    return render(request, 'biblio/copia_nueva.html', {'form': form})


def actualizar_autor(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    if request.method == "POST":
        form = PickAutorForm(request.POST)
        id_dic = dict(form.data)
        id_list = id_dic["autores"]
        for id in id_list:
            autor = get_object_or_404(Autor, pk=id)
            autor.libros_publicados.add(libro)
    form = PickAutorForm()
    context = {'form' : form, 'libro': libro}
    return render(request, 'biblio/detalle_libro.html', context)
