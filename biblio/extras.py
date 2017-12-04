from .models import Libro, Copia, Socio, Prestamo, Devolucion, Autor
from datetime import datetime, date, time, timedelta

def puedo_prestar(socio, copia):
    if socio.estado == False and copia.estado == False:
        return True
    else:
        return False

def socio_moroso(socio, copia, fecha):
    copia_id = copia.id
    prestamo = Prestamo.objects.get(copia='copia_id', estado=False)
    if fecha > prestamo.fecha_fin:
        socio.estado=True
        socio.save()
        return False
    else:
        return True
    
def futuro_moroso(fm):
    hoy = date.today()   
    morosos = []
    for socio in fm:
        socio_id = socio.id 
        prestamo = Prestamo.objects.get(socio='socio_id', estado=False)
        if prestamo.fecha_fin <= hoy:
            morosos.append(socio)
    return morosos