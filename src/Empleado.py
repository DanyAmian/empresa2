__author__ = 'Daniel'


class Empleado:
    """
       Esta es la clase Empleado, utilizada para crear empleados.

       Los empleados que se crearan en esta clase seran incorporados a los departamentos de la clase departamentos.

    """
    def __init__(self, nombre, apellidos, dni, direccion, edad, email, salario):
        """Construtor de la clase Empleado

        :param nombre: Este es el atributo para indicar el nombre del Empleado
        :param apellidos: Este es el atributo para indicar los apellidos del Empleado
        :param dni: Este es el atributo para indicar el dni del Empleado
        :param direccion: Este es el atributo para indicar la direccion del Empleado
        :param edad: Este es el atributo para indicar la edad del Empleado
        :param email: Este es el atributo para indicar el email del Empleado
        :param salario: Este es el atributo para indicar el salario del Empleado
        :return: Este es el constructor, por lo que no devuelve nada
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.edad = edad
        self.email = email
        self.salario = salario

    def get_salario(self):
        """Metodo que devolvera el salario del Empleado

        :return: Devolvera el salario del Empleado
        """
        return self.salario

    def get_dni(self):
        """Metodo que devolvera el dni del Empleado

        :return: Devolvera el dni del Empleado
        """
        return self.dni

    def get_nombre(self):
        """Metodo que devolvera el nombre del Empleado

        :return: Devolvera el nombre del Empleado
        """
        return self.nombre + " " + self.apellidos

    # ## EPD3
    def get_edad(self):
        """Metodo que devolvera la edad del Empleado

        :return: Devolvera la edad del Empleado
        """
        return self.edad

    def get_email(self):
        """Metodo que devolvera el email del Empleado

        :return: Devolvera el email del Empleado
        """
        return self.email

    def get_direccion(self):
        """Metodo que devolvera la direccion del Empleado

        :return: Devolvera la direccion del Empleado
        """
        return self.direccion

    def get_salario_mensual(self):
        """Metodo que devolvera el salario mensual del Empleado

        :return: Devolvera el salario mensual del Empleado
        """
        return self.salario
