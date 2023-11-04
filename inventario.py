# -*- coding: utf-8 -*-

class Inventario:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def seguimiento_existencias(self, libro, libros):
        for libro in self.libros:
            print(libro)