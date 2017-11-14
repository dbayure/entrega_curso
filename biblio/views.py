from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.http import HttpResponse


from .models import Libro, Copia, Socio, Prestamo, Devolucion

def index(request):
    return render(request, 'biblio/index.html')

def libros(request):
    total_libros = Libro.objects.order_by('-titulo')[:5]
    context = {'lista_libros' : total_libros}
    return render(request, 'biblio/listado_libros.html', context)

def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    return render(request, 'biblio/detalle_libro.html', {'libro': libro})

class ResultsView(generic.DetailView):
    model = Socio
    template_name = 'biblio/socios.html'
