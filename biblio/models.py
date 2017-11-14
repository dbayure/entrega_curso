from django.db import models
DATE_INPUT_FORMATS = ('%d-%m-%Y')

# Create your models here.
class Libro(models.Model):
    ISBN = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    fecha_de_ingreso = models.DateTimeField()
    
    def __str__(self):
        return "%s %s" % (self.titulo, self.autor)

#Prestado falso por omision
class Copia(models.Model):
    inventario = models.IntegerField(default=0)
    ISBN = models.ForeignKey(Libro, on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.ISBN
    
#Morososo falso por omision
class Socio(models.Model):
    CI = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    correo = models.EmailField()
    fecha_nacimiento = models.DateTimeField()
    estado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre
    
#Prestado falso por omision
class Prestamo(models.Model):
    ISBN = models.CharField(max_length=200)
    CI = models.CharField(max_length=200)
    fecha_comienzo = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    estado = models.BooleanField(default=False)
    
    def __str__(self):
        return "%s %s" % (self.ISBN, self.CI)
    
class Devolucion(models.Model):
    ISBN = models.CharField(max_length=200)
    CI = models.CharField(max_length=200)
    fecha_devolucion = models.DateTimeField()
    
    def __str__(self):
        return "%s %s" % (self.ISBN, self.CI)
    