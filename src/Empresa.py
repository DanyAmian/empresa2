__author__ = 'Dany'


class Empresa:
    """
       Esta es la clase Empresa, utilizada para gestionar empleados y departamentos.

       Las empresas que se crean en esta clase podran tener empleados y departamentos

    """
    def __init__(self, nombre_empresa, cif, razon_social):
        """

        :param nombre_empresa: Este es el atributo para indicar el nombre de la Empresa
        :param cif: Este es el atributo para indicar el cif de la Empresa
        :param razon_social: Este es el atributo para indicar la razon social de la Empresa
        :return: Este es el constructor, por lo que no devuelve nada
        """
        self.nombre_empresa = nombre_empresa
        self.cif = cif
        FALLO PROVOCADO!
        self.razon_social = razon_social
        self.lista_departamentos = []

    def get_nombre_empresa(self):
        """Metodo que devolvera el nombre de la Empresa

        :return: Devolvera el nombre de la Empresa
        """
        return self.nombre_empresa

    def get_cif(self):
        """Metodo que devolvera el cif de la Empresa

        :return: Devolvera el cif de la Empresa
        """
        return self.cif

    def get_razon_social(self):
        """Metodo que devolvera la razon social de la Empresa

        :return: Devolvera la razon social de la Empresa
        """
        return self.razon_social

    def aniadir_departamento(self, departamento):
        """Metodo que aniadira un departamento a la Empresa

        :return: Devolvera la lista de departamentos con el nuevo departamento incluido
        """
        self.lista_departamentos.append(departamento)