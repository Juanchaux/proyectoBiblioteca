# -*- coding: utf-8 -*-

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.subcategoria = []
        
    def __str__(self):
        return f"Categoria: {self.nombre}\nLibros: {','.join(lib.titulo for lib in self.libros)}"

    def getNombre(self):
        return self.nombre
    
    def agregarLibro(self, libro):
        self.libros.append(libro)

    def agregarSubcategoria(self, subcategoria):
        self.subcategoria.append(subcategoria)