"""entrega_curso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

app_name = 'biblio'
urlpatterns = [
    # ex: /biblio/
    url(r'^$', views.index, name='index'),
    # ex: /biblio/prestamos
    url(r'^prestamos/$', views.prestamos, name='prestamos'),
    # ex: /biblio/prestamo/5
    url(r'^prestamo/(?P<prestamo_id>[0-9]+)/$', views.detalle_prestamo, name='detalle_prestamo'),
    # ex: /biblio/prestamo/nuevo    
    url(r'^prestamo/nuevo$', views.prestamo_nuevo, name='prestamo_nuevo'),
    # ex: /biblio/devoluciones
    url(r'^devoluciones$', views.devoluciones, name='devoluciones'),
    # ex: /biblio/devolucion/nueva
    url(r'^devolucion/(?P<devolucion_id>[0-9]+)/$', views.detalle_devolucion, name='detalle_devolucion'),
    # ex: /biblio/devolucion/nueva
    url(r'^devolucion/nueva$', views.devolucion_nueva, name='devolucion_nueva'),
    # ex: /biblio/socios
     url(r'^socios/activos$', views.activos, name='activos'),
    # ex: /biblio/morosos
    url(r'^socios/morosos$', views.morosos, name='morosos'), 
    # ex: /biblio/socio/5
    url(r'^socio/(?P<socio_id>[0-9]+)/$', views.detalle_socio, name='detalle_socio'),
    # ex: /biblio/futuros morosos
    url(r'^socios/futuros_morosos$', views.futuros_morosos, name='futuros_morosos'),    
    # ex: /biblio/socio/nuevo
    url(r'^socio/nuevo$', views.socio_nuevo, name='socio_nuevo'),
        # ex: /biblio/autores
     url(r'^autores$', views.autores, name='autores'),
    # ex: /biblio/autor/5
    url(r'^autor/(?P<autor_id>[0-9]+)/$', views.detalle_autor, name='detalle_autor'),  
    # ex: /biblio/socio/nuevo
    url(r'^autor/nuevo$', views.autor_nuevo, name='autor_nuevo'),
    # ex: /biblio/copia/5
    url(r'^(?P<inventario_id>[0-9]+)/$', views.detalle_copia, name='detalle_cpia'),  
    # ex: /biblio/libro/5
    url(r'^libro/(?P<libro_id>[0-9]+)/$', views.detalle_libro, name='detalle_libro'),
    #ex: /bilblio/libros
    url(r'^libros/$', views.libros, name='libros'),
    # ex: /biblio/libro/nuevo
    url(r'^libro/nuevo$', views.libro_nuevo, name='libro_nuevo'),
    # ex: /biblio/autor/5
    url(r'^autor/(?P<autor_id>[0-9]+)/$', views.detalle_autor, name='detalle_autor'),
    # ex: /biblio/autores
     url(r'^autores$', views.autores, name='autores'),
     # ex: /biblio/autor/nuevo
    url(r'^autor/nuevo$', views.autor_nuevo, name='autor_nuevo'),
    # ex: /biblio/autores_libros
    url(r'^autores_libros/$', views.autores_libros, name='autores_libros'),
    # ex: /biblio/autores_libros
    url(r'^autores_libros/(?P<autor_id>[0-9]+)/(?P<libro_id>[0-9]+)/$', views.autores_libros_nuevo, name='autores_libros_nuevo'),
]
