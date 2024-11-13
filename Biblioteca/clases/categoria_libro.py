import tipo_categoria

class Categoria_libro(tipo_categoria):
    def _init_(self,id_categoria, id_tipo_categoria, categoria_libro): # <---encapsulamiento atributos en el constructor
        tipo_categoria.Tipo_categoria.__init__(id_tipo_categoria)
        self.id_categoria = id_categoria
        self.categoria_libro = categoria_libro
        