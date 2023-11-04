# -*- coding: utf-8 -*-

class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo, fecha_devolucion_prevista):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion_prevista = fecha_devolucion_prevista

    def __str__(self) -> str:
        return f"Usuario: {self.usuario}\nLibro: {self.libro}\nFecha de prestamo: {self.fecha_prestamo}\nFecha de devolucion prevista: {self.fecha_devolucion_prevista}\n\n"
    
    def getUsuario(self):
        return self.usuario
    
    def getFechaDevolucion(self):
        return self.fecha_devolucion_prevista
    
    def realizar_prestamo(self):
        if self.libro.getNumCopias() > 0:
           self.libro.setNumCopias(self.libro.getNumCopias() - 1)
           return True
        else:
           return False

    def devolucion(self):
        self.libro.setNumCopias(self.libro.getNumCopias() + 1)

    def buscarPrestamo(usuario, prestamos):
        listPrestamo = []
        for pres in prestamos:
            if pres.getUsuario() == usuario:
                listPrestamo.append(pres)
        if len(listPrestamo) > 0:
            return listPrestamo
        return None
    

    def numPrestamosLibro(libro, prestamos):
        numPrestamos = 0
        for pres in prestamos:
            if pres.libro.getTitulo() == libro.getTitulo():
                numPrestamos += 1
        return numPrestamos