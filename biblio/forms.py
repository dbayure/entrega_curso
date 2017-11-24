from django.forms import ModelForm

from .models import Prestamo, Libro, Devolucion, Socio, Autor, Autores_Libros

class PrestamoForm(ModelForm):
    class Meta:
        model = Prestamo
        fields = ['ISBN', 'CI', 'fecha_comienzo', 'fecha_fin', 'estado']
        
class LibroForm(ModelForm):
    class Meta:
        model = Libro
        fields = ['ISBN', 'titulo', 'fecha_de_ingreso']

class DevolucionForm(ModelForm):
    class Meta:
        model = Devolucion
        fields = ['ISBN', 'CI', 'fecha_devolucion']  

class SocioForm(ModelForm):
    class Meta:
        model = Socio
        fields = ['CI', 'nombre', 'correo', 'fecha_nacimiento', 'estado']  

class AutorForm(ModelForm):
    class Meta:
        model = Socio
        fields = ['CI', 'nombre', 'correo', 'fecha_nacimiento']  

class Autor_LibroForm(ModelForm):
    class Meta:
        model = Autores_Libros
        fields = ['autores', 'libros'] 