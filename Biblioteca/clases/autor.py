import  paises   #-----> calse padre

class Autor(paises):    #----->calse hija (Herencia) 
    def __init__(self,id_autor,nom_autor,seudonimo,id_pais , fecha_nac, fecha_def, biografia_autor):
        super().__init__(id_pais)  
        self.id_autor = id_autor
        self.nom_autor = nom_autor
        self.seudonimo = seudonimo
        self.fecha_nac = fecha_nac
        self.fecha_def = fecha_def
        self.biografia_autor = biografia_autor
            