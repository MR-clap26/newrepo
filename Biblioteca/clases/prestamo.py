


import detalle_libro
import usuario

class Prestamo(detalle_libro, usuario):
    def __init__(self, id_prestamo, isbn, id_user, fecha_prestamo, fecha_devolucion, fecha_devuelto, cantidad):
        detalle_libro.__init__(isbn)
        usuario.__init__(id_user)
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.fecha_devuelto = fecha_devuelto
        self.cantidad = cantidad
        
    def calcular_fechas(self):
     pass