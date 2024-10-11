import tipo_categoria

class categoria_libro(tipo_categoria):
    def _init_(self,id_categoria, id_tipo_categoria, categoria_libro):
        super().__init__(id_tipo_categoria)
        self.id_categoria = id_categoria
        self.categoria_libro = categoria_libro
        