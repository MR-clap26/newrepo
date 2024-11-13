import libro
import editorial

class DetalleLibro(libro, editorial):
    def __init__(self, id_detalle_libro, isbn, fecha_edicion, id_editorial, numero_paginas, id_categoria_libro, num_ejemplares, ejem_disponibles):
        libro.Libro.__init__(isbn)
        editorial.Editorial.__init__(id_editorial)
        self.id_detalle_libro = id_detalle_libro
        self.fecha_edicion = fecha_edicion
        self.numero_paginas = numero_paginas
        self.id_categoria_libro = id_categoria_libro
        self.num_ejemplares = num_ejemplares
        self.ejem_disponibles = ejem_disponibles
    
    def modificar_disponibilidad(self):        
        pass