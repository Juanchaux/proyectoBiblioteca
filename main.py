# -*- coding: utf-8 -*-
import os
from datetime import datetime

from imports import Categoria, Usuario, Libro, Prestamo, Multa, Correo, ReporteLibro, ReporteUsuario, ReporteGenero, InterfazUsuario

correo = Correo()

ReportesLibros = []
ReportesUsuarios = []
ReportesGeneros = []
ReportesAutores = []
usuarios = []
libros = []
categorias = [Categoria("Terror"), Categoria("Novelas")]
multas = []

# Creación de usuarios de prueba
usuario1 = Usuario("Cristian David", 1109540572, "juan.chaux@utp.edu.co", 3102820764)
usuarios.append(usuario1)
ReportesUsuarios.append(ReporteUsuario(usuario1))
usuario2 = Usuario("Pedrito Pérez", 12345, "example@example.com")
usuarios.append(usuario2)
ReportesUsuarios.append(ReporteUsuario(usuario2))

# Creación de libros de prueba
libro1 = Libro("IT", "Stephen King", "Terror", "CFT0001TR", 57)
libros.append(libro1)
ReportesLibros.append(ReporteLibro(libro1))
categorias[0].agregarLibro(libro1)
libro2 = Libro("100 años de soledad", "Gabriel García Márquez", "Novela", "NBL0001NV")
libros.append(libro2)
ReportesLibros.append(ReporteLibro(libro2))
categorias[1].agregarLibro(libro2)
libro3 = Libro("El coronel no tiene quien le escriba", "Gabriel García Márquez", "Novela", "NBL0002NV")
libros.append(libro3)
ReportesLibros.append(ReporteLibro(libro3))
categorias[1].agregarLibro(libro3)
libro4 = Libro("Carrie", "Stephen King", "Terror", "CFT0001TR", 57)
libros.append(libro4)
ReportesLibros.append(ReporteLibro(libro4))
categorias[0].agregarLibro(libro4)

# Creación de prestamos de prueba
fecha1 = datetime(2023, 10, 15)
fecha2 = datetime(2023, 10, 20)
prestamos = [Prestamo(usuario1,libro1,fecha1,fecha2)]


# Funcion utilizada para esperar a que el usuario presione enter para continuar y limpiar la pantalla de la consola
def esperar():
    input("Presione enter para continuar...")
    
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

while True:
    print(InterfazUsuario.menuPrincipal())
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "0":
        break
    
    elif opcion == "1":
        print(InterfazUsuario.menuUsuarios())
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "0":
            break

        elif opcion == "1":
            nombre = input("Ingrese el nombre del usuario: ")
            documento = int(input("Ingrese el número de documento: "))
            correo = input("Ingrese su correo electrónico: ")
            telefono = int(input("Ingrese su numero de teléfono: "))
            nuevo_usuario = Usuario(nombre, documento, correo, telefono)
            usuarios.append(nuevo_usuario)
            ReportesUsuarios.append(ReporteUsuario(nuevo_usuario))
            print("Usuario creado exitosamente.")
            esperar()

        elif opcion == "2":
            print("Ingrese el documento del usuario a modificar")
            documento = int(input())
            usuario = Usuario.buscarUsuario("documento", documento, usuarios)
            if usuario:
                usuario = usuario[0]
                print("Desea modificar todo el usuario? (s/n)")
                opcion = input()

                if opcion == "s":
                    if usuario:
                        nombre = input("Ingrese el nuevo nombre: ")
                        documento = int(input("Ingrese el nuevo documento: "))
                        correo = input("Ingrese el nuevo correo: ")
                        telefono = int(input("Ingrese el nuevo telefono: "))
                        usuario.editarUsuario(nombre, documento, correo, telefono)
                        print("Usuario modificado")
                        esperar()
                    else:
                        print("Usuario no encontrado")
                        esperar()
                else:
                    print("Ingrese el campo a modificar")
                    print("0. Nombre")
                    print("1. Identificacion")
                    print("2. Correo")
                    print("3. Telefono")
                    opcion = input()

                    if opcion == "0":
                        if usuario:
                            nombre = input("Ingrese el nuevo nombre: ")
                            usuario.setNombre(nombre)
                            print("Usuario modificado")
                            esperar()
                    if opcion == "1":
                        if usuario:
                            documento = int(input("Ingrese el nuevo documento: "))
                            usuario.setIdentificacion(documento)
                            print("Usuario modificado")
                            esperar()

                    if opcion == "2":
                        if usuario:
                            correo = input("Ingrese el nuevo correo: ")
                            usuario.setCorreo(correo)
                            print("Usuario modificado")
                            esperar()
                    if opcion == "3":
                        if usuario:
                            telefono = int(input("Ingrese el nuevo telefono: "))
                            usuario.setTelefono(telefono)
                            print("Usuario modificado")
                            esperar()
            else:
                print("Usuario no encontrado")
                esperar()

        elif opcion == "3":
            print("Ingrese el documento del usuario a eliminar")
            documento = int(input())
            usuario = Usuario.buscarUsuario("documento", documento, usuarios)
            if usuario:
                usuario = usuario[0]
                usuarios.remove(usuario)
                print("Usuario eliminado")
                esperar()
            else:
                print("Usuario no encontrado")
                esperar()

        elif opcion == "4":
            print("Seleccione el criterio de busqueda para el usuario: ")
            print("0. Nombre")
            print("1. Identificacion")
            criterio = input("Ingrese la opción: ")
            
            if criterio == "0":
                criterio = "nombre"
                nombre_usuario = input("Ingrese el nombre del usuario: ")
                listUsuarios = Usuario.buscarUsuario(criterio, nombre_usuario, usuarios)
                if listUsuarios:
                    print("Usuarios encontrados: \n")
                    for user in listUsuarios:
                        print(user)
                    esperar()
                else:
                    print(f"No se encontró ningún usuario con el nombre {nombre_usuario}.\n")
                    esperar()
            if criterio == "1":
                criterio = "documento"
                ident = int(input("Ingrese el documento del usuario: "))
                listUsuarios = Usuario.buscarUsuario(criterio, ident, usuarios)
                if listUsuarios:
                    print("Usuarios encontrados: \n")
                    for user in listUsuarios:
                        print(user)
                    esperar()
                else:
                    print(f"No se encontró ningún usuario con el documento {ident}.\n")
                    esperar()
        elif opcion=="5":
            print("Lista de usuarios: \n")
            for user in usuarios:
                print(user)
            esperar()

    elif opcion == "2":
        print(InterfazUsuario.menuLibros())
        opcion = input("Seleccione una opcion: ")

        if opcion == "0":
            break

        if opcion == "1":
            titulo = input("Ingrese el titulo del libro: ")
            autor = input("Ingrese el nombre del autor: ")
            print("Ingrese el genero del libro: ")
            for i in range(len(categorias)):
                print(f"{i} {categorias[i].getNombre()}")
            opcGenero = int(input("Opcion categoria: "))
            ISBN = input("Ingrese el código del libro (ISBN): ")
            num_copias = int(input("Digite el número de copias de libro: "))
            nuevo_libro = Libro(titulo, autor, categorias[opcGenero].getNombre(), ISBN, num_copias)
            libros.append(nuevo_libro)
            ReportesLibros.append(ReporteLibro(nuevo_libro))
            categorias[opcGenero].agregarLibro(nuevo_libro)
            
            print("Libro registrado exitosamente.")
            esperar()
        
        elif opcion == "2":
            print("Ingrese el ISBN del libro a modificar")
            ISBN = input()
            libro = Libro.buscarLibro("ISBN", ISBN, libros)
            if libro:
                libro = libro[0]
                print("Desea modificar todo el libro? (s/n)")
                opcion = input()

                if opcion == "s":
                    if libro:
                        titulo = input("Ingrese el nuevo titulo: ")
                        autor = input("Ingrese el nuevo autor: ")
                        print("Ingrese el nuevo genero del libro: ")
                        for i in range(len(categorias)):
                            print(f"{i} {categorias[i].getNombre()}")
                        opcGenero = int(input("Opcion categoria: "))
                        ISBN = input("Ingrese el nuevo código del libro (ISBN): ")
                        num_copias = int(input("Digite el nuevo número de copias de libro: "))
                        libro.editarLibro(titulo, autor, categorias[opcGenero].getNombre(), ISBN, num_copias)
                        print("Libro modificado")
                        esperar()
                    else:
                        print("Libro no encontrado")
                        esperar()
                else:
                    print("Ingrese el campo a modificar")
                    print("0. Titulo")
                    print("1. Autor")
                    print("2. Genero")
                    print("3. ISBN")
                    print("4. Numero de copias")
                    opcion = input()

                    if opcion == "0":
                        if libro:
                            titulo = input("Ingrese el nuevo titulo: ")
                            libro.setTitulo(titulo)
                            print("Libro modificado")
                            esperar()
                    if opcion == "1":
                        if libro:
                            autor = input("Ingrese el nuevo autor: ")
                            libro.setAutor(autor)
                            print("Libro modificado")
                            esperar()

                    if opcion == "2":
                        if libro:
                            print("Ingrese el nuevo genero del libro: ")
                            for i in range(len(categorias)):
                                print(f"{i} {categorias[i].getNombre()}")
                            opcGenero = int(input("Opcion categoria: "))
                            libro.setGenero(categorias[opcGenero].getNombre())
                            print("Libro modificado")
                            esperar()
                    if opcion == "3":
                        if libro:
                            ISBN = input("Ingrese el nuevo ISBN: ")
                            libro.setISBN(ISBN)
                            print("Libro modificado")
                            esperar()
                    if opcion == "4":
                        if libro:
                            num_copias = int(input("Ingrese el nuevo numero de copias: "))
                            libro.setNumCopias(num_copias)
                            print("Libro modificado")
                            esperar()
                    else:
                        print("Libro no encontrado")
                        esperar()
            else:
                print("Libro no encontrado")
                esperar()
    
        elif opcion == "3":
            print("Ingrese el ISBN del libro a eliminar")
            ISBN = input()
            libro = Libro.buscarLibro("ISBN", ISBN, libros)
            if libro:
                libro = libro[0]
                libros.remove(libro)
                print("Libro eliminado")
                esperar()
            else:
                print("Libro no encontrado")
                esperar()

        elif opcion == "4":
            print("Seleccione el criterio de busqueda para el libro: ")
            print("0. Titulo")
            print("1. Autor")
            print("2. Genero")
            criterio = input("Ingrese la opción: ")
            criterio = "titulo" if criterio== "0" else "autor" if criterio == "1" else "genero"

            if criterio == "titulo":
                titulo_libro = input("Ingrese el titulo del libro: ")
                libro_encontrado = Libro.buscarLibro(criterio, titulo_libro, libros)
                if libro_encontrado:
                    for libro in libro_encontrado:
                        print(libro)
                    esperar()
                else:
                    print(f"No se encontró ningún libro con el titulo {titulo_libro}.\n")
                    esperar()
            elif criterio == "autor":
                aut = input("Ingrese el nombre del autor: ")
                libro_encontrado = Libro.buscarLibro(criterio, aut, libros)
                if libro_encontrado:
                    for libro in libro_encontrado:
                        print(libro)
                    esperar()
            elif criterio == "genero":
                gen = input("Ingrese el Genero: ")
                libro_encontrado = Libro.buscarLibro(criterio, gen, libros)
                if libro_encontrado:
                    for libro in libro_encontrado:
                        print(libro)
                    esperar()
                else:
                    print(f"No se encontró ningún libro del genero {aut}.\n")
                    esperar()
        
        elif opcion == "5":
            print("Seleccione el criterio de busqueda para el libro: ")
            print("0. Autor")
            print("1. Genero")
            criterio = input("Ingrese la opción: ")
            criterio = "autor" if criterio== "0" else "genero"

            valorBusqueda = input("Ingrese el Autor: ") if criterio == "autor" else input("Ingrese el Genero: ")
            listaFiltrada = Libro.listarLibros(criterio, valorBusqueda, libros);
            if listaFiltrada:
                print("Libros encontrados: \n")
                for lib in listaFiltrada:
                    print(lib)
                esperar()
            else:
                print("No se encontro el libro")
                esperar()

    elif opcion == "3":
        print(InterfazUsuario.menuPrestamos())
        opcion = input("Seleccione una opcion: ")

        if opcion == "0":
            break
        
        elif opcion == "1":
            print("Ingrese el documento del usuario: ")
            documento = int(input())
            usuario = Usuario.buscarUsuario("documento", documento, usuarios)
            usuario = usuario[0] if usuario else None
            tieneMultas = Multa.buscarMulta(usuario, multas)
            tienePrestamos = Prestamo.buscarPrestamo(usuario, prestamos)
            if usuario and not tieneMultas and not tienePrestamos:
                print("Criterio de busqueda del libro: ")
                print("0. Titulo")
                print("1. Autor")
                print("2. Genero")
                criterio = input()
                criterio = "titulo" if criterio == "0" else "autor" if criterio == "1" else "genero"
                valorBusqueda = input("Ingrese el valor de busqueda: ")
                libro = Libro.buscarLibro(criterio, valorBusqueda, libros)
                if libro:
                    libro = libro[0]
                    print("La fecha de prestamo será la fecha actual.")
                    fecha_prestamo = datetime.now()  # Obtiene la fecha y hora actual
                    
                    while True:
                        print("Ingrese la fecha de devolucion en formato 'dd/mm/yyyy': ")
                        fecha_devolucion_str = input()
                        fecha_devolucion = datetime.strptime(fecha_devolucion_str, "%d/%m/%Y")
                        if fecha_devolucion > fecha_prestamo:
                            break
                        else:
                            print("La fecha de devolucion debe ser mayor a la fecha de prestamo")
                    
                    prestamo = Prestamo(usuario, libro, fecha_prestamo, fecha_devolucion)
                    if prestamo.realizar_prestamo():
                        reporteLib = ReporteLibro.buscarReporte(ReportesLibros, libro)
                        reporteLib.agregarPrestamo()
                        reporteUs = ReporteUsuario.buscarReporte(ReportesUsuarios, usuario)
                        reporteUs.agregarPrestamo()
                        reporteGen = ReporteGenero.buscarReporte(ReportesGeneros, libro.getGenero())
                        reporteGen.agregarPrestamo()
                        print("Prestamo realizado")
                        esperar()
                        prestamos.append(prestamo)
                    else:
                        print("No se pudo realizar el prestamo")
                        esperar()
            else:
                print("El usuario no existe o tiene multas o prestamos pendientes")
                esperar()
        
        elif opcion == "2":
            print("Ingrese el documento del usuario: ")
            documento = int(input())
            usuario = Usuario.buscarUsuario("documento", documento, usuarios)
            if usuario:
                prestamo = Prestamo.buscarPrestamo(usuario[0], prestamos)
                if prestamo:
                    prestamo = prestamo[0]
                    prestamo.devolucion()

                    banderaMulta = False
                    fecha_actual = datetime.today()
                    if fecha_actual > prestamo.getFechaDevolucion():
                        diasEnMora = abs((prestamo.getFechaDevolucion() - fecha_actual).days)
                        multa = Multa(usuario[0], diasEnMora * 2000)
                        correo.sendEmail(usuario[0], multa, diasEnMora)
                        multas.append(multa)
                        banderaMulta = True
                    prestamos.remove(prestamo)

                    print(f"Libro devuelto { 'y multa generada' if banderaMulta else '' }")
                    esperar()
                else:
                    print("No se encontró ningún prestamo para el usuario")
                    esperar()
            else:
                print("Usuario no encontrado")
                esperar()

        elif opcion == "3":
            print("Ingrese el documento del usuario: ")
            documento = int(input())
            usuario = Usuario.buscarUsuario("documento", documento, usuarios)
            if usuario:
                prestamo = Prestamo.buscarPrestamo(usuario[0], prestamos)
                if prestamo:
                    prestamo = prestamo[0]
                    print(prestamo)
                    esperar()
                else:
                    print("No se encontró ningún prestamo para el usuario")
                    esperar()
            else:
                print("Usuario no encontrado")
                esperar()
        elif opcion == "4":
            print("Lista de prestamos: \n")
            for pres in prestamos:
                print(pres)
            esperar()

    elif opcion == "4":
        print(InterfazUsuario.menuMultas())
        opcion = input("Seleccione una opcion: ")

        if opcion == "0":
            break
        
        elif opcion == "1":
            print("Ingrese el documento del usuario: ")
            documento = int(input())
            usuario = Usuario.buscarUsuario("documento", documento, usuarios)
            if usuario:
                multa = Multa.buscarMulta(usuario[0], multas)
                if multa:
                    multa = multa[0]
                    multas.remove(multa)
                    print("Multa pagada")
                    esperar()
                else:
                    print("El usuario no tiene multas")
                    esperar()
            else:
                print("Usuario no encontrado")
                esperar()
        
        elif opcion == "2":
            print("Ingrese el documento del usuario: ")
            documento = int(input())
            usuario = Usuario.buscarUsuario("documento", documento, usuarios)
            if usuario:
                multa = Multa.buscarMulta(usuario[0], multas)
                if multa:
                    multa = multa[0]
                    print(multa)
                    esperar()
                else:
                    print("El usuario no tiene multas")
                    esperar()
            else:
                print("Usuario no encontrado")
                esperar()

        elif opcion == "3":
            print("Lista de multas: \n")
            for mult in multas:
                print(mult)
            esperar()

    elif opcion == "5":
        print(InterfazUsuario.menuReportes())
        opcion = input("Seleccione una opcion: ")

        if opcion == "0":
            break
        
        elif opcion == "1":
            reportes_libros_ordenados = sorted(ReportesLibros, key=lambda reporte: reporte.getPrestamosRealizados(), reverse=True)

            for reporte in reportes_libros_ordenados:
                print(f"Libro: {reporte.libro.getTitulo()}, Prestamos: {reporte.getPrestamosRealizados()}")
            esperar()

        elif opcion == "2":
            reportes_generos_ordenados = sorted(ReportesGeneros, key=lambda reporte: reporte.getPrestamosRealizados(), reverse=True)

            for reporte in reportes_generos_ordenados:
                print(f"Genero: {reporte.genero}, Prestamos: {reporte.getPrestamosRealizados()}")
            esperar()
            
    elif opcion == "6":
        print(InterfazUsuario.menuInventario())
        opcion = input("Seleccione una opcion: ")

        if opcion == "0":
            break
        
        elif opcion == "1":
            print("Lista de libros: \n")
            for lib in libros:
                print(f"Titulo: {lib.getTitulo()}, Numero de Copias: {lib.getNumCopias() + Prestamo.numPrestamosLibro(lib, prestamos)}, Disponibles: {lib.getNumCopias()}, Prestamos: {Prestamo.numPrestamosLibro(lib, prestamos)}\n")
            esperar()

    elif opcion == "7":
        print(InterfazUsuario.menuCategorias())
        opcion = input("Seleccione una opcion: ")

        if opcion == "0":
            break
            
        elif opcion == "1":
            nombre = input("Ingrese el nombre de la categoria: ")
            categorias.append(Categoria(f"{nombre}"))

        elif opcion == "2":
            print("Lista de categorias: \n")
            for cat in categorias:
                print(cat)
            esperar()


    # if opcion == "3":
    #     categoria = input("Ingrese el nombre de la categoria: ")
    #     categorias.append(Categoria(f"{categoria}"))      
        


# Pendientes:
# - Crear reportes estadisticos ( libro que mas multas tiene generadas )
# - cambiar las multas para que se generen luego de 3 dias
# - Cambiar que cada usuario pueda tener maximo 3 prestamos
# - Cambiar las multas para que tambien traigan el libro por el cual se genero la multa
# - Inventario para notificar cuando un libro esta a punto de agotarse ( 10 unidades )
# - Inventario para notificar cuando un libro se agota

