# -*- coding: utf-8 -*-

class Usuario:
    def __init__(self, nombre=None, identificacion=None, correo=None, telefono=None):
        self.nombre = nombre
        self.identificacion = identificacion
        self.correo = correo
        self.telefono = telefono if telefono is not None else 0
    
    def __str__(self):        
        return f"Nombre: {self.nombre}\nIdentificación: {self.identificacion}\nCorreo: {self.correo}\nTeléfono: {self.telefono}\n\n"


    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getIdentificacion(self):
        return self.identificacion
    
    def setIdentificacion(self, identificacion):
        self.identificacion = identificacion
    
    def getCorreo(self):
        return self.correo
    
    def setCorreo(self, correo):
        self.correo = correo
    
    def getTelefono(self):
        return self.telefono
    
    def setTelefono(self, telefono):
        self.telefono = telefono

    def editarUsuario(self, nombre, identificacion, correo, telefono):
        self.nombre = nombre
        self.identificacion = identificacion
        self.correo = correo
        self.telefono = telefono

    @staticmethod
    def buscarUsuario(criterio,valor, usuarios):
        listaUs = []
        if criterio == "nombre":
            for usuario in usuarios:
                if usuario is not None and usuario.getNombre().lower() == valor.lower():
                    listaUs.append(usuario)
            return listaUs if listaUs else None
        if criterio == "documento":
            for usuario in usuarios:
                if usuario is not None and usuario.getIdentificacion() == valor:
                    listaUs.append(usuario)
            return listaUs if listaUs else None

    @staticmethod
    def eliminarUsuario(usuario, usuarios):
        for i in range(len(usuarios)):
            if usuarios[i] == usuario:
                usuarios[i] = None
                break