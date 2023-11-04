# -*- coding: utf-8 -*-

class InterfazUsuario:
    def menuPrincipal():
        return f"1.Gestion de Usuarios\n2.Gestion de Libros\n3.Gestion de Prestamos\n4.Gestion de Multas\n5.Gestion de Reportes Estadisticos\n6.Gestion de Inventario\n7.Gestion de Categorias\n0.Salir\n"

    def menuUsuarios():
        return f"1.Agregar Usuario\n2.Modificar Usuario\n3.Eliminar Usuario\n4.Buscar Usuario\n5.Listar Usuarios\n0.Salir\n"
    
    def menuLibros():
        return f"1.Agregar Libro\n2.Modificar Libro\n3.Eliminar Libro\n4.Buscar Libro\n5.Listar Libros\n0.Salir\n"
    
    def menuPrestamos():
        return f"1.Agregar Prestamo\n2.Eliminar Prestamo\n3.Buscar Prestamo\n4.Listar Prestamos\n0.Salir\n"\
        
    def menuMultas():
        return f"1.Eliminar Multa\n2.Buscar Multa\n3.Listar Multas\n0.Salir\n"
    
    def menuReportes():
        return f"1.Libros mas Populares\n2.Generos mas Populares\n3.Autores mas Populares\n4.Reporte 4\n5.Reporte 5\n0.Salir\n"
    
    def menuInventario():
        return f"1.Ver cantidad de libros\n2.Modificar Libro\n3.Eliminar Libro\n4.Buscar Libro\n5.Listar Libros\n0.Salir\n"
    
    def menuCategorias():
        return f"1.Agregar Categoria\n2.Agregar Subcategoria\n3.Eliminar Categoria\n4.Buscar Categoria\n5.Listar Categorias\n0.Salir\n"