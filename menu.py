from datetime import date
from clienteCorporativo import ClienteCorp
from clienteParticular import ClientePart
from repositorioClientes import RepositorioClientes
from editarCliente import guardar_c
from editarTrabajo import guardar_t
import sys

class Menu:
    # Mostrar un menú y responder a las opciones
     def __init__(self):
        self.lista_clientes = guardar_c()
        self.lista_trabajo = guardar_t()
        self.repoc = RepositorioClientes()
        self.opciones = {
                "0": self.salir,
                "1": self.mostrar_clientes,
                "2": self.nuevo_cliente,
                "3": self.editar_cliente_particular,
                "4": self.eliminar_cliente,
                "5": self.editar_cliente_corporativo,
                "6": self.buscar_cliente,
                "7": self.agregar_trabajo,
                "8": self.mostrar_trabajo,
                "9": self.editar_trabajo,
                "10": self.trabajo_retirado,
                "11": self.trabajo_terminado,
                "12": self.buscar_trabajo,

        }

     def mostrar_menu(self):
        print("""
        
Menú Clientes:                              Menu Trabajos:

1. Mostrar clientes                     8.  Mostrar trabajo
2. Nuevo cliente                        9.  Editar o cancelar trabajo
3. Cambiar cliente particular           10.  Irabajo retirado
4  Eliminar cliente                     11. Terminar trabajo
5. Cambiar cliente corporativo          12. Buscar trabajo
6. Buscar cliente                       
7. Agregar trabajo                      

                            0.Salir
                                                : """)



     def mostrar_clientes(self, lista=None):

        if lista == None:
            lista = self.lista_clientes.lista
        for cliente in lista:
            print(cliente)
            print("-----------------------------------------")

     def nuevo_cliente(self):

        tipo = "A"
        while tipo not in ("C", "c", "P", "p"):
            tipo = input("Ingrese el tipo de cliente: C:Corporativo / P: Particular: ")
        if tipo in ("C", "c"):
            nombre = input("Ingrese el nombre de la empresa: ")
            contacto = input("Ingrese el nombre del contacto: ")
            tel_contacto = input("Ingrese el teléfono del contacto: ")
        else:
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
        tel = input("Ingrese el teléfono: ")
        mail = input("Ingrese el correo electrónico: ")
        if tipo in ("C", "c"):
            c = self.lista_clientes.nuevo_cliente_corp(nombre, contacto, tel_contacto, tel, mail)
        else:
            c = self.lista_clientes.nuevo_cliente_part(nombre, apellido, tel, mail)
        if c is None:
            print(" Error al cargar el cliente")
        else:
            print(c)
            print(" Cliente cargado correctamente")

     def editar_cliente_particular(self):

        id_cliente = int(input("Ingrese el ID del cliente particular que desea modificar: "))
        opc = int(input(""""Seleccionar que quiere editar:
                            1. Nombre
                            2. Apellido
                            3. Teléfono
                            4. Mail
                            5. Eliminar cliente
                            0. Salir
                            : """))
        if opc == 1:
            nombre = input("Ingrese el nuevo nombre: ")
            c = self.lista_clientes.cambiar_nombre(nombre, id_cliente)
            if c == None:
                print("Error al editar cliente")
            else:
                print("Cliente editado correctamente")
        if opc == 2:
            apellido = input("Ingrese el nuevo apellido: ")
            c = self.lista_clientes.cambiar_apellido(apellido, id_cliente)
            if c == None:
                print("Error al editar cliente")
            else:
                print("Cliente editado correctamente")
        if opc == 3:
            telefono = input("Ingrese el nuevo telefono: ")
            c = self.lista_clientes.cambiar_telefono(telefono, id_cliente)
            if c == None:
                print("Error al editar cliente")
            else:
                print("Cliente editado correctamente")
        if opc == 4:
            mail=input("Ingrese el nuevo mail: ")
            c=self.lista_clientes.cambiar_mail(mail, id_cliente)
            if c == None:
                print("Error al editar cliente")
            else:
                print("Cliente editado correctamente")

        if opc == 5:
            self.lista_clientes.eliminar_cliente(id_cliente)
            c=self.lista_clientes.eliminar_cliente(id_cliente)
            self.lista_clientes= guardar_c()
            if c == None:
                print("Error al borrar cliente")
            else:
                print("Cliente borrado")

     def eliminar_cliente(self):
        """Solicita el id del contacto y elimina el contacto"""
        id_cliente = int(input("ingrese el id del cliente"))
        c = self.repoc.get_one(id_cliente)
        if c == None:
            print("el id es inexistente")
        else:
            self.repoc.delete(c)
            self.lista_clientes.lista = self.repoc.get_all()
            print("contacto eliminado")

     def editar_cliente_corporativo(self):

        id_cliente=int(
            input("Ingrese el ID del cliente corporativo que desea modificar: "))
        opc=int(input(""""Elija una opción para modificar o eliminar un trabajo:
                        1. Nombre de empresa
                        2. Nombre de contacto
                        3. Teléfono de contacto
                        4. Teléfono
                        5. Mail
                        6. Borrar cliente
                        0. Salir
                        :   """))
        if opc == 1:
            nombre_empresa=input("Ingrese el nuevo nombre de la empresa: ")
            c=self.lista_clientes.cambiar_nombre_empresa(nombre_empresa, id_cliente)
            if c is None:
                print("Error al editar cliente")
            else:
                 print("Cliente editado correctamente")
        if opc == 2:
            nombre_contacto=input("Ingrese el nuevo nombre del contacto: ")
            c=self.lista_clientes.cambiar_nombre_contacto(nombre_contacto, id_cliente)
            if c is None:
                print("Error al editar cliente")
            else:
                print("Cliente editado correctamente")
        if opc == 3:
            telefono_contacto=input("Ingrese el nuevo teléfono del contacto: ")
            c=self.lista_clientes.cambiar_telefono_contacto(telefono_contacto, id_cliente)
            if c is None:
                print("Error al editar cliente")
            else:
                print("Cliente editado correctamente")
        if opc == 4:
            telefono=input("Ingrese el nuevo telefono: ")
            c=self.lista_clientes.cambiar_telefono(telefono, id_cliente)
            if c is None:
                print("Error al editar cliente")
            else:
                print("Cliente editado correctamente")
        if opc == 5:
            mail=input("Ingrese el nuevo mail: ")
            c=self.lista_clientes.cambiar_mail(mail, id_cliente)
            if c is None:
                print("Error al editar cliente")
            else:
                print("Cliente editado correctamente")
        if opc == 6:
            self.lista_clientes.eliminar_cliente(id_cliente)
            c=self.lista_clientes.eliminar_cliente(id_cliente)
            self.lista_clientes= guardar_c()
            if c is None:
                print("Error al borrar cliente")
            else:
                print("Cliente borrado")

     def buscar_cliente(self):

         listas=self.lista_clientes.lista
         for clientec in listas:
             print(clientec)
         opc=int(input(""""Elija una opción para buscar un cliente:
                                1. Id del cliente
                                2. Telefono
                                3. Mail
                                0. Salir
                                : """))
         if opc == 1:
             filtro=int(input("Ingrese ID: "))
             for i in listas:
                 if i.id_cliente == filtro:
                     print(i)
         if opc == 2:
             filtro=input("Ingrese telefono: ")
             for i in listas:
                 if i.telefono == filtro:
                     print(i)
         if opc == 3:
             filtro=input("Ingrese mail: ")
             for i in listas:
                 if i.mail == filtro:
                     print(i)

     def agregar_trabajo(self):

        listatrabajo=self.lista_clientes.lista
        for cliente in listatrabajo:
             print(cliente)
        filtro=int(input("Buscar ID: "))
        for f in listatrabajo:
            if f.id_cliente == filtro:
                print(f)
                cliente=f
        fecha_ingreso=date.today()
        print("Fecha de entrega propuesta")
        anio=int(input("Ingrese el año: "))
        mes=int(input("Ingrese el mes: "))
        if mes <= 13 and mes >= 1:
            dia=int(input("Ingrese el día: "))
            if dia <= 31 and dia >= 1:
                fecha_entrega_propuesta=date(anio, mes, dia)
                descripcion=input("Ingrese una descripcion del trabajo: ")
                t=self.lista_trabajo.NuevoTrabajo(cliente, fecha_ingreso, fecha_entrega_propuesta, descripcion)
                if t is None:
                    print("Error al cargar trabajo")
                else:
                    print("Trabajo cargado correctamente")
            else:
                print("Ingrese un día del 1 al 30")
        else:
            print("Ingrese un mes del 1 al 12")

     def buscar_trabajo(self):
        print("Buscar trabajo")
        listas=self.lista_trabajo.listatrabajo
        opc=int(input(""""Elija una opcion para buscar un trabajo:
                         1. ID trabajo
                         2. Descrpcion
                         0. Salir
                         : """))
        if opc == 1:
            filtro=int(input("Ingrese ID: "))
            for i in listas:
                if i.id_trabajo == filtro:
                    print(i)
        if opc == 2:
            filtro=input("Ingrese descripcion: ")
            for i in listas:
                if i.descripcion == filtro:
                    print(i)

     def mostrar_trabajo(self, listatrabajo=None):

        if listatrabajo == None:
            listatrabajo = self.lista_trabajo.listatrabajo
        for trabajo in listatrabajo:
          print(trabajo)

     def editar_trabajo(self):
        lista = self.lista_trabajo.listatrabajo
        for tr in lista:
            print(tr)
        id_trabajo = int(input("Ingrese el ID del trabajo a modificar: "))
        a = int(input(""""Elija una opción para editar o eliminar un trabajo:
                         1. Descripcion
                         2. Fecha de ingreso
                         3. Eliminar trabajo
                         0. Salir 
                         : """))
        if a == 1:
            descrpicion = input("Ingrese la nueva descripción: ")
            t = self.lista_trabajo.cambiar_descripcion(descrpicion, id_trabajo)
            if t == None:
                print("Error al editar trabajo")
            else:
                print("Trabajo modificado")
        if a == 2:
            anio = int(input("Ingrese el año : "))
            mes = int(input("Ingrese el mes: "))
            dia = int(input("Ingrese el dia: "))
            t = self.lista_trabajo.cambiar_fecha_ingreso(date(anio, mes, dia), id_trabajo)
            if t == None:
                print("Error al editar trabajo")
            else:
                print("Trabajo modificado")
        if a == 3:
            self.lista_trabajo.borrar_trabajo(id_trabajo)
            t = self.lista_trabajo.borrar_trabajo(id_trabajo)
            self.lista_trabajo = guardar_t()
            if t == None:
                print("Error al borrar cliente")
            else:
                print("Cliente borrado")

     def trabajo_terminado(self):

         listas=self.lista_trabajo.listatrabajo
         for clientec in listas:
             print(clientec)
         id_trabajo=int(
             input("Ingrese el ID del trabajo a terminar: "))
         fecha_entrega_real=date.today()
         t=self.lista_trabajo.trabajo_terminado(fecha_entrega_real, id_trabajo)
         if t == None:
            print("Error al terminar el trabajo")
         else:
                print("Trabajo terminado")

     def trabajo_retirado(self):

        listas=self.lista_trabajo.listatrabajo
        for clientec in listas:
            print(clientec)
        id_trabajo=int(input("Ingrese el ID del trabajo a retirar: "))
        t=self.lista_trabajo.trabajo_entregado(True, id_trabajo)
        if t == None:
            print("Error al retirar trabajo")
        else:
            print("Trabajo retirado")

     def ejecutar(self):

        while True:
            self.mostrar_menu()
            opcion = input("Ingresar una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("{0} opción invalida".format(opcion))

     def salir(self):
        print("Cerrando sistema.")
        sys.exit(0)

if __name__ == "__main__":
    m= Menu()
    m.ejecutar()