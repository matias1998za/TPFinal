from trabajo import Trabajo
from repositorioTrabajos import RepositorioTrabajos

class guardar_t:
    def __init__(self):
        self.rt = RepositorioTrabajos()
        self.listatrabajo = self.rt.get_all()


    def NuevoTrabajo(self, cliente, fecha_ingreso, fecha_entrega_propuesta, descripcion):

        nt = Trabajo(cliente, fecha_ingreso, fecha_entrega_propuesta, None, descripcion, False)
        nt.id_trabajo = self.rt.store(nt)
        if nt.id_trabajo == 0:
            return None
        else:
            self.listatrabajo.append(nt)
            return nt





    def cambiar_descripcion(self, descripcion, id_trabajo):

        cd = self.buscar_por_id(id_trabajo)
        if cd:
            cd.descripcion = descripcion
            return self.rt.update(cd)
        return False


    def cambiar_fecha_ingreso(self, fecha_ingreso, id_trabajo):

        cf = self.buscar_por_id(id_trabajo)
        if cf:
            cf.fecha_ingreso = fecha_ingreso
            return self.rt.update(cf)
        return False


    def borrar_trabajo(self, id_trabajo):

        bt = self.buscar_por_id(id_trabajo)
        if bt:
            return self.rt.update(bt)
        return False


    def trabajo_terminado(self, fecha_entrega_real, id_trabajo):

        tt = self.buscar_por_id(id_trabajo)
        if tt:
            tt.fecha_entrega_real = fecha_entrega_real
            return self.rt.update(tt)
        return None


    def trabajo_entregado(self, retirado, id_trabajo):

        te = self.buscar_por_id(id_trabajo)
        if te:
            te.retirado = retirado
            return self.rt.update(te)
        return None

    def buscar_por_id(self, id_trabajo):

        for buscar_id in self.listatrabajo:
            if buscar_id.id_trabajo == int(id_trabajo):
                return (buscar_id)
        return None