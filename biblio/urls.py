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
    #url(r'^prestamos$', views.index, name='prestamos'),
    # ex: /biblio/prestamo/id/isbn
    #url(r'^(?P<socio_id>[0-9]+)/(?P<isbn>[0-9]+)/$', views.index, name='prestamo'),
    # ex: /biblio/devoluciones
    #url(r'^devoluciones$', views.index, name='devoluciones'),
    # ex: /biblio/devolucion/id/inventario
    #url(r'^(?P<socio_id>[0-9]+)/(?P<inventario_id>[0-9]+)/$', views.index, name='devolucion'),
    # ex: /biblio/socios
     url(r'^(?P<pk>[0-9]+)/socios/$', views.ResultsView.as_view(), name='socios'),
    # ex: /biblio/futuros morosos
    #url(r'^futuros_morosos$', views.index, name='futuros_morosos'),    
    # ex: /biblio/socios/5
    #url(r'^(?P<socio_id>[0-9]+)/$', views.detail, name='detalle_socio'),
    # ex: /biblio/copia/5
    #url(r'^(?P<inventario_id>[0-9]+)/$', views.detail, name='detalle_cpia'),  
    # ex: /biblio/libro/5
    url(r'^libro/(?P<libro_id>[0-9]+)/$', views.detalle_libro, name='detalle_libro'),
    #ex: /bilblio/libros
    url(r'^libros/$', views.libros, name='libros'),
]
