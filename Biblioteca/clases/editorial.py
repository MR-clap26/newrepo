import paises

class Editorial(paises):
    def __init__(self, id_editorial, nom_editorial, fecha_fundacion, id_pais, telefono_contacto, correo_contacto): # <---encapsulamiento atributos en el constructor
        paises.Paises.__init__(id_pais)
        self.id_editorial = id_editorial
        self.nom_editorial = nom_editorial
        self.fecha_fundacion = fecha_fundacion
        self.telefono_contacto = telefono_contacto
        self.correo_contacto = correo_contacto
    
    def validar_contacto(self):
        pass