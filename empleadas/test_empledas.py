import pytest

from .models import Empleada, Jefa


def test_obtener_presupuesto_empleada():
    sueldo = 2000
    empleada = Empleada('Luciana', sueldo)
    assert sueldo == empleada.calcular_presupuesto()


def test_obtener_presupuesto_jefa():
    sueldo_empleda = 2000
    sueldo_jefa = 4000
    empleada = Empleada('Luciana', sueldo_empleda)
    jefa = Jefa('Jefota', sueldo_jefa)
    assert sueldo_jefa == jefa.calcular_presupuesto()


def test_obtener_presupuesto_jefa_con_empleada():
    sueldo_empleda = 2000
    sueldo_jefa = 4000
    empleada = Empleada('Luciana', sueldo_empleda)
    jefa = Jefa('Jefota', sueldo_jefa)
    jefa.agregar_empleada(empleada)
    assert sueldo_jefa + sueldo_empleda == jefa.calcular_presupuesto()


def test_obtener_presupuesto_jefa_con_empleada_con_empleadas():
    sueldo_empleda = 2000
    sueldo_empleda_jefa = 3000
    sueldo_jefa = 4000
    empleada = Empleada('Luciana', sueldo_empleda)
    empleada_jefa = Jefa('Josefa', sueldo_empleda_jefa)
    empleada_jefa.agregar_empleada(empleada)
    jefa = Jefa('Jefota', sueldo_jefa)
    jefa.agregar_empleada(empleada_jefa)

    assert sueldo_empleda_jefa + sueldo_empleda == empleada_jefa.calcular_presupuesto()
    assert sueldo_jefa + sueldo_empleda_jefa + sueldo_empleda == jefa.calcular_presupuesto()


def test_agregar_empleada_no_soportada():
    jefa = Jefa('test', 1000)
    with pytest.raises(Exception) as e_info:
        jefa.agregar_empleada('test no valido')

    assert str(e_info.value) == 'Necesita usar una persona con sueldo'


