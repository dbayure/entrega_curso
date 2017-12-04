from django import forms

from .models import Prestamo, Libro, Devolucion, Socio, Autor, Copia

class PrestamoForm(forms.ModelForm):
    
    class Meta:
        model = Prestamo
        fields = ['copia', 'socio', 'fecha_comienzo', 'fecha_fin', 'estado']
        
class PrestamoIdForm(forms.ModelForm):

    class Meta:
        model = Prestamo
        fields = ['socio', 'fecha_comienzo', 'fecha_fin', 'estado']
        exclude = ['copia']
        
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['ISBN', 'titulo', 'resumen', 'fecha_de_ingreso']

class CopiaForm(forms.ModelForm):
    class Meta:
        model = Copia
        fields = ['inventario', 'ISBN', 'estado']  
        
class DevolucionForm(forms.ModelForm):
    class Meta:
        model = Devolucion
        fields = ['copia', 'socio', 'fecha_devolucion']  

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['CI', 'nombre', 'correo', 'fecha_nacimiento', 'estado']  

class AutorForm(forms.ModelForm):
    libros_publicados = forms.ModelMultipleChoiceField(queryset=Libro.objects.all())
    
    class Meta:
        model = Autor
        fields = ['CI', 'nombre', 'correo', 'resumen', 'fecha_nacimiento', 'libros_publicados']  

class PickAutorForm(forms.ModelForm):
    autores = forms.ModelMultipleChoiceField(queryset=Autor.objects.all(), required=False)
    
    class Meta:
        model = Autor
        fields = ['autores']
        
        
        
        
         