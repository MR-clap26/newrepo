import paises
import tipo_usuario
from rut_chile import rut_chile

class Usuario(paises, tipo_usuario):
    def __init__(self, id_user, nombre, correo, telefono, rut , id_pais , id_tipo , fecha_crea): # <---encapsulamiento atributos en el constructor
        paises.Paises.__init__(id_pais)
        tipo_usuario.Tipo_usuario.__init__(id_tipo)
        self.id_user = id_user
        self.nombre = nombre
        self.correo= correo
        self.telefono= telefono
        self.rut = rut
        self.fecha_crea = fecha_crea
    
    def validacion_rut(self):
        return rut_chile.is_valid_rut(self.rut_usuario)
    
    def validacion_correo(self):
        pass