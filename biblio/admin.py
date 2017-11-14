from django.contrib import admin

from .models import Libro, Copia, Socio, Prestamo, Devolucion

admin.site.register(Libro)
admin.site.register(Copia)
admin.site.register(Socio)
admin.site.register(Prestamo)
admin.site.register(Devolucion)