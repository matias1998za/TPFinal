#! /usr/bin/python3

import datetime

class Trabajo:

    def __init__(self, cliente, fecha_ingreso, fecha_entrega_propuesta,
        fecha_entrega_real, descripcion, retirado, id_trabajo = None):
        self.cliente = cliente
        self.fecha_ingreso = fecha_ingreso
        self.fecha_entrega_propuesta = fecha_entrega_propuesta
        self.fecha_entrega_real = fecha_entrega_real
        self.descripcion = descripcion
        self.retirado = retirado
        self.id_trabajo = id_trabajo

    def __str__(self):
            cadena = f"ID del trabajo: {self.id_trabajo}\nDescripción: {self.descripcion}\n {self.cliente}\n"
            cadena += f"Fechas:\nFecha de ingreso: {self.fecha_ingreso} \n fecha de entrega propuesta {self.fecha_entrega_propuesta} \n fecha de entrega real {self.fecha_entrega_real}\n"
            cadena += f" retirado - {self.retirado}\n"
            return cadena








