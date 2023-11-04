# -*- coding: utf-8 -*-

class ReporteLibro:
    def __init__(self, libro):
        self.libro = libro
        self.prestamosRealizados = 0

    def __str__(self):
        return f"Libro: {self.libro.titulo} - Prestamos: {self.prestamosRealizados}"

    def getPrestamosRealizados(self):
        return self.prestamosRealizados
    
    def buscarReporte(reportes, libro):
        for reporte in reportes:
            if reporte.libro.getTitulo() == libro.getTitulo():
                return reporte
        return None
    
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
            if reporte.usuario.getNombre() == usuario.getNombre():
                return reporte
        return None
    
class ReporteGenero:
    def __init__(self, genero):
        self.genero = genero
        self.prestamosRealizados = 0

    def __str__(self):
        return f"Genero: {self.genero} - Prestamos: {self.prestamosRealizados}"

    def getPrestamosRealizados(self):
        return self.prestamosRealizados
    
    def agregarPrestamo(self):
        self.prestamosRealizados += 1

    def buscarReporte(reportes, genero):
        for reporte in reportes:
            if reporte.genero == genero:
                return reporte
        return None
    