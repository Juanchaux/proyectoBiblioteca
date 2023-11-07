from unidecode import unidecode

# -*- coding: utf-8 -*-
class Libro:
    def __init__(self, titulo=None, autor=None, genero=None, ISBN=None, num_copias=0):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ISBN = ISBN
        self.num_copias = num_copias
        
    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, ISBN: {self.ISBN}, " \
               f"Copias Disponibles: {self.num_copias}"

    def getTitulo(self):
        return self.titulo
    def getAutor(self):
        return self.autor
    def getGenero(self):
        return self.genero
    def getISBN(self):
        return self.ISBN
    def getNumCopias(self):
        return self.num_copias
    def setNumCopias(self, num_copias):
        self.num_copias = num_copias
    
    @staticmethod
    def buscarLibro(criterio,valor, libros):
        listaLibs = []
        if criterio == "titulo":
            for libro in libros:
                if libro is not None and unidecode(libro.getTitulo().lower()) == unidecode(valor.lower()):
                    listaLibs.append(libro)
            return listaLibs if listaLibs else None
        
        if criterio == "autor":
            for libro in libros:
                if libro is not None and unidecode(libro.getAutor().lower()) == unidecode(valor.lower()):
                    listaLibs.append(libro)
            return listaLibs if listaLibs else None
        
        if criterio == "genero":
            for libro in libros:
                if libro is not None and unidecode(libro.getGenero().lower()) == unidecode(valor.lower()):
                    listaLibs.append(libro)
            return listaLibs if listaLibs else None
        
        if criterio == "ISBN":
            for libro in libros:
                if libro is not None and unidecode(libro.getISBN().lower()) == unidecode(valor.lower()):
                    listaLibs.append(libro)
            return listaLibs if listaLibs else None

    @staticmethod
    def listarLibros(criterio,valor, libros):
        listaLibs = []
        if criterio == "autor":
            for libro in libros:
                if libro is not None and unidecode(libro.getAutor().lower()) == unidecode(valor.lower()):
                    listaLibs.append(libro)
            return listaLibs if listaLibs else None
        
        if criterio == "genero":
            for libro in libros:
                if libro is not None and unidecode(libro.getGenero().lower()) == unidecode(valor.lower()):
                    listaLibs.append(libro)
            return listaLibs if listaLibs else None
        
    @staticmethod
    def modificarLibro(libro, titulo, autor, genero, ISBN, num_copias):
        libro.setTitulo(titulo)
        libro.setAutor(autor)
        libro.setGenero(genero)
        libro.setISBN(ISBN)
        libro.setNumCopias(num_copias)
        return libro