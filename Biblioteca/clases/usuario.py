class usuario:
    def __init__(self,id_user,nombre,ap_pat,ap_mat,fecha_nac,num_telfono,correo,direccion,tipo_user):
        self.id_user=id_user
        self.nombre=nombre
        self.ap_pat=ap_pat
        self.ap_mat=ap_mat
        self.fecha_nac=fecha_nac
        self.num_telefono=num_telfono
        self.correo=correo
        self.direccion=direccion
        self.tipo_user=tipo_user


import paises
import tipo_usuario

from rut_chile import rut_chile

class Usuario(paises, tipo_usuario):
    def __init__(self, id_user, nombre, correo, telefono, rut,id_pais, habilitado, id_tipo_usuario, fecha_creacion):
        paises.__init__(id_pais)
        tipo_usuario.__init__(id_tipo_usuario)
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.correo_usuario = correo_usuario
        self.telefono_usuario = telefono_usuario
        self.rut_usuario = rut_usuario
        self.habilitado = habilitado
        self.fecha_creacion = fecha_creacion
    
    def validacion_rut(self):
        return rut_chile.is_valid_rut(self.rut_usuario)
    
    def validacion_correo(self):