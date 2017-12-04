from django.db import models
from email.policy import default
DATE_INPUT_FORMATS = ('%d-%m-%Y')

# Create your models here.
class Libro(models.Model):
    ISBN = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    resumen = models.CharField(max_length=400, default='')
    fecha_de_ingreso = models.DateTimeField()
    
    def __str__(self):
        return "%s" % (self.titulo)

#Prestado falso por omision
class Copia(models.Model):
    inventario = models.IntegerField(default=0)
    ISBN = models.ForeignKey(Libro, on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.ISBN)
    
#Morososo falso por omision
class Socio(models.Model):
    CI = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    correo = models.EmailField()
    fecha_nacimiento = models.DateTimeField()
    #Moroso
    estado = models.BooleanField(default=False)
    
    def __str__(self):
        return (self.nombre)
    
#Autor
class Autor(models.Model):
    CI = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    correo = models.EmailField()
    resumen = models.CharField(max_length=400, default='')
    fecha_nacimiento = models.DateTimeField()
    libros_publicados = models.ManyToManyField(Libro)

    def __str__(self):
        return (self.nombre)    
    
#Terminado falso por omision
class Prestamo(models.Model):
    copia = models.ForeignKey(Copia, on_delete=models.CASCADE)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    fecha_comienzo = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    #pendiente o terminado)
    estado = models.BooleanField(default=False)
    
    def __str__(self):
        return "%s %s" % (self.copia, self.socio)
    
    @classmethod
    def create(cls, ISBN, CI, fecha_comienzo):
        prestamo = cls(ISBN=ISBN, CI=CI, fecha_comienzo=fecha_comienzo)
        # do something with the book
        return prestamo
    
class Devolucion(models.Model):
    copia = models.ForeignKey(Copia, on_delete=models.CASCADE)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    fecha_devolucion = models.DateTimeField()
    
    def __str__(self):
        return "%s %s" % (self.copia, self.socio)

    