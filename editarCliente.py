from clienteParticular import ClientePart
from clienteCorporativo import ClienteCorp
from repositorioClientes import RepositorioClientes

class guardar_c:
    def __init__(self):
     self.rc = RepositorioClientes()
     self.lista = self.rc.get_all()

    def nuevo_cliente_corp(self, nombre_empresa, nombre_contacto, telefono_contacto, telefono, mail):
        nc = ClienteCorp(nombre_empresa, nombre_contacto, telefono_contacto, telefono, mail)
        nc.id_cliente = self.rc.store(nc)
        if nc.id_cliente == 0:
            return False
        else:
            self.lista.append(nc)
            return nc

    def nuevo_cliente_part(self, nombre, apellido, telefono, mail):
        np = ClientePart(nombre, apellido, telefono, mail)
        np.id_cliente = self.rc.store(np)
        if np.id_cliente == 0:
            return False
        else:
            self.lista.append(np)
            return np

    def eliminar_cliente(self, id_cliente):
        ''' elimina un cliente cancelado'''
        cl = self.buscar_por_id(id_cliente)
        if cl:
            return self.rc.delete(cl)

        return None

    def buscar_por_id(self, id_cliente):

        for bid in self.ClienteL:
            if bid.id_cliente == int(id_cliente):
                return (bid)
        return None

    def cambiar_nombre(self, nombre, id_cliente):
        clientes = self.buscar_por_id(id_cliente)
        if clientes:
            clientes.nombre = nombre
            return self.rc.update(clientes)
        return None

    def cambiar_nombre_empresa(self, nombre_empresa, id_cliente):
        clientes = self.buscar_por_id(id_cliente)
        if clientes:
            clientes.nombre_empresa = nombre_empresa
            return self.rc.update(clientes)
        return False


    def cambiar_apellido(self, apellido, id_cliente):
        clientes = self.buscar_por_id(id_cliente)
        if clientes:
            clientes.apellido = apellido
            return self.rc.update(clientes)
        return False

    def cambiar_telefono(self, telefono, id_cliente):
        clientes = self.buscar_por_id(id_cliente)
        if clientes:
            clientes.telefono = telefono
            return self.rc.update(clientes)
        return False

    def cambiar_mail(self, mail, id_cliente):
        clientes = self.buscar_por_id(id_cliente)
        if clientes:
            clientes.mail = mail
            return self.rc.update(clientes)
        return False


    def cambiar_telefono_contacto(self, telefono_contacto, id_cliente):
        clientes = self.buscar_por_id(id_cliente)
        if clientes:
            clientes.telefono_contacto = telefono_contacto
            return self.rc.update(clientes)
        return False

    def cambiar_nombre_contacto(self, nombre_contacto, id_cliente):
        clientes = self.buscar_por_id(id_cliente)
        if clientes:
            clientes.nombre_contacto = nombre_contacto
            return self.rc.update(clientes)
        return False


    def buscar(self, filtro):
        notas_e = []
        for c_notas in self.lista:
            if c_notas.coincide(filtro):
                notas_e.append(c_notas)
        return notas_e
