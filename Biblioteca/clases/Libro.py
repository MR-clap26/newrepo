import autor # <------- clase padre/super_clase (herencia) 

class Libro(autor): # <------clase hija (herencia)
    def __init__(self, isbn, titulo, id_autor): # <---encapsulamiento atributos en el constructor
        autor.Autor.__init__(id_autor)
        self.isbn = isbn
        self.titulo = titulo
    
    def validar_isbn(self):
 
        if(10 == len(self.isbn)):
            return True
        else:
            return False
        