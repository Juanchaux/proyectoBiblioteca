# -*- coding: utf-8 -*-
from unidecode import unidecode

class ReporteLibro:
    def __init__(self, libro):
        self.libro = libro
        self.prestamosRealizados = 0
        self.multasRealizadas = 0

    def __str__(self):
        return f"Libro: {self.libro.titulo} - Prestamos: {self.prestamosRealizados}"

    def getPrestamosRealizados(self):
        return self.prestamosRealizados
    
    def getMultasRealizadas(self):
        return self.multasRealizadas
    
    def buscarReporte(reportes, libro):
        for reporte in reportes:
            if unidecode(reporte.libro.getTitulo()) == unidecode(libro.getTitulo()):
                return reporte
        return None
    
    def agregarMultas(self):
        self.multasRealizadas += 1
    
    def agregarPrestamo(self):
        self.prestamosRealizados += 1
    
class ReporteUsuario:
    def __init__(self, usuario):
        self.usuario = usuario
        self.prestamosRealizados = 0

    def __str__(self):
        return f"Usuario: {self.usuario.nombre} - Prestamos: {self.prestamosRealizados}"

    def getPrestamosRealizados(self):
        return self.prestamosRealizados
    
    def agregarPrestamo(self):
        self.prestamosRealizados += 1

    def buscarReporte(reportes, usuario):
        for reporte in reportes:
            if unidecode(reporte.usuario.getNombre()) == unidecode(usuario.getNombre()):
                return reporte
        return None
    
class ReporteGenero:
    def __init__(self, genero):
        self.genero = genero
        self.prestamosRealizados = 0

    def __str__(self):
        return f"Genero: {self.genero} - Prestamos: {self.prestamosRealizados}"

    def getGenero(self):
        return self.genero
    
    def getPrestamosRealizados(self):
        return self.prestamosRealizados
    
    def agregarPrestamo(self):
        self.prestamosRealizados += 1

    def buscarReporte(reportes, genero):
        for reporte in reportes:
            if reporte.getGenero() == genero:
                return reporte
        return None