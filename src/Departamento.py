__author__ = 'Daniel'


class Departamento:
    """
       Esta es la clase Departamento, utilizada para crear y gestionar los departamentos.

       Los departamentos de la empresa contienen empleados asociados.

    """
    def __init__(self, nombre_depto, id_depto):
        """

        :param nombre_depto: Este es el atributo para indicar el nombre del Departamento
        :param id_depto: Este es el atributo para indicar el identificador del Departamento
        :return: Este es el constructor, por lo que no devuelve nada
        """
        self.nombre_depto = nombre_depto
        self.id_depto = id_depto
        self.lista_empleados = []

    def get_nombre_depto(self):
        """Metodo que devolvera el nombre del Departamento.

        :return: Devolvera el nombre del Departamento
        """
        return self.nombre_depto

    def get_id_depto(self):
        """Metodo que devolvera el identificador del Departamento

        :return: Devolvera el identificador del Departamento
        """
        return self.id_depto

    def aniadir_empleado(self, empleado):
        """Metodo que aniadira un empleado a la lista de empleados del departamento

        :return: Devolvera la lista de empleados con el nuevo empleado aniaadido al departamento.
        """
        self.lista_empleados.append(empleado)

    def get_salario_total(self):
        """Metodo que devolvera el salario total de todos los empleados del Departamento

        :return: Devolvera el total de salario del Departamento, sumando el salario de todos los empleados
        """
        total = 0
        for empleado in self.lista_empleados:
            total += empleado.get_salario()
        return total

    # #EPD3
    def get_salario_total_mensual(self):
        """Metodo que devolvera el salario total de todos los empleados del Departamento de forma mensual

        :return: Devolvera el total de salario del Departamento, sumando el salario de todos los empleados de forma mensual
        """
        total = 0
        for empleado in self.lista_empleados:
            total += empleado.get_salario_mensual()
        return total