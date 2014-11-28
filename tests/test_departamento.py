from unittest import TestCase
from mockito import *
from src.Empleado import *
from src.Departamento import *


__author__ = 'aulas'


class TestDepartamento(TestCase):
    """
       Esta es la clase test_Departamento, utilizada para comprobar ciertos metodos de la clase Departamento

       Los departamentos tienen ciertos metodos que deben ser comprobados

    """
    def test_get_salario_total(self):
        """Este metodo comprobara que el metodo get_salario_total realiza la funcion de obtener
        todos los salarios acumulados de forma correcta.
        Se han utilizado objetos mocks para simular objetos reales, para facilitar la comprobacion.
        Para no comprar con dos objetos simulados, he creado una variable acumulador y conforme
        se crean los mocks se va incrementando. Esta variable la comparo con el total devuelto por el metodo.

        :return: No devuelve nada
        """
        # Generate a mock from a class
        acumulado = 0
        emp1 = mock(Empleado)
        emp2 = mock(Empleado)
        emp3 = mock(Empleado)
        dept1 = Departamento("Calidad", 1)
        # Mock method calls
        when(emp1).get_salario().thenReturn(28000)
        acumulado += 28000
        when(emp2).get_salario().thenReturn(28000)
        acumulado += 28000
        when(emp3).get_salario().thenReturn(28000)
        acumulado += 28000

        dept1.aniadir_empleado(emp1)
        dept1.aniadir_empleado(emp2)
        dept1.aniadir_empleado(emp3)

        res = dept1.get_salario_total()
        print("TEST EPD2")
        print("Salario emp1: " + str(emp1.get_salario()))
        print("Salario emp2: " + str(emp2.get_salario()))
        print("Salario emp3: " + str(emp3.get_salario()))
        print("Salario total devuelto por getsalariototal(): " + str(res))
        self.assertEquals(res, acumulado)

        # EPD3

    def test_get_salario_total_mensual(self):
        """Este metodo comprobara que el metodo get_salario_total_mensual realiza la funcion de obtener
        todos los salarios mensuales acumulados de forma correcta.
        Se han utilizado objetos mocks para simular objetos reales, para facilitar la comprobacion.
        Para no comprar con dos objetos simulados, he creado una variable acumulador y conforme
        se crean los mocks se va incrementando. Esta variable la comparo con el total devuelto por el metodo.

        :return: No devuelve nada
        """
        # Generate a mock from a class
        acumulado2 = 0
        emp4 = mock(Empleado)
        emp5 = mock(Empleado)
        emp6 = mock(Empleado)
        dept2 = Departamento("Calidad 2", 4)
        # Mock method calls
        when(emp4).get_salario_mensual().thenReturn(2000)
        acumulado2 += 2000
        when(emp5).get_salario_mensual().thenReturn(2000)
        acumulado2 += 2000
        when(emp6).get_salario_mensual().thenReturn(2000)
        acumulado2 += 2000

        dept2.aniadir_empleado(emp4)
        dept2.aniadir_empleado(emp5)
        dept2.aniadir_empleado(emp6)

        res = dept2.get_salario_total_mensual()
        print("TEST EPD3")
        print("Salario mensual emp4: " + str(emp4.get_salario_mensual()))
        print("Salario mensual emp5: " + str(emp5.get_salario_mensual()))
        print("Salario mensual emp6: " + str(emp6.get_salario_mensual()))
        print("Salario total devuelto por get_salario_total_mensual(): " + str(res))
        self.assertEquals(res, acumulado2)