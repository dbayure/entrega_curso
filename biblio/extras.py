from .models import Libro, Copia, Socio, Prestamo, Devolucion, Autor
from datetime import datetime, date, time, timedelta

def puedo_prestar(socio, copia):
    if socio.estado == False and copia.estado == False:
        return True
    else:
        return False

def socio_moroso(socio, copia, fecha):
    copia_id = copia.id
    prestamo = Prestamo.objects.filter(copia_id=copia_id, estado=False).first()
    if prestamo:
        if fecha > prestamo.fecha_fin.date():
            socio.estado=True
            socio.save()
    
def futuro_moroso(fm):
    hoy = date.today()   
    morosos = []
    for socio in fm:
        socio_id = socio.id 
        prestamo = Prestamo.objects.filter(socio_id=socio_id, estado=False).first()
        if prestamo:
            if prestamo.fecha_fin.date() <= hoy:
                morosos.append(socio)
    return morosos