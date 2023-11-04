# -*- coding: utf-8 -*-

class Multa:
    def __init__(self, usuario, cantidad):
        self.usuario = usuario
        self.cantidad = cantidad
    
    def getUsuario(self):
        return self.usuario
    
    def getCantidad(self):
        return self.cantidad
    
    def buscarMulta(usuario, multas):
        listMultas = []
        
        for multa in multas:
            if multa.getUsuario() == usuario:
                listMultas.append(multa)
        
        if len(listMultas) > 0:
            return listMultas
        else:
            return None