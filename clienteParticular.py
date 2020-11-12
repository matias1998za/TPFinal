#! /usr/bin/env python3
from cliente import Cliente

class ClientePart(Cliente):

    def __init__(self, nombre, apellido, telefono, mail, id_cliente = None):
        self.nombre = nombre
        self.apellido = apellido
        super().__init__(telefono, mail, id_cliente)

    def __str__(self):
        cadena = f"ID del cliente: {self.id_cliente}\nNombre: {self.nombre}\nApellido: {self.apellido}\nTipo de cliente: (Cliente particular)\n"
        cadena += f"Contactos: \n Teléfono: {self.telefono}\n Mail: {self.mail}\n"
        return cadena
