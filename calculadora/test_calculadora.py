from .calculadora import (
    Calculadora,
    Potencia,
    RaizCuadrada,
    RaizCubo,
    Raiz,
    Suma,
    Resta,
    Multiplicacion,
    Division,
    DecoratorCotaMax,
    DecoratorCotaMin
)
import pytest

def test_suma_2_mas_2_igual_4():
    resultado = Calculadora().operar(Suma(2, 2))
    assert resultado == 4


def test_resta_4_menos_2_igual_2():
    resultado = Calculadora().operar(Resta(4, 2))
    assert resultado == 2


def test_multiplica_3_por_2_igual_6():
    resultado = Calculadora().operar(Multiplicacion(3, 2))
    assert resultado == 6


def test_divide_9_por_3_igual_3():
    resultado = Calculadora().operar(Division(9, 3))
    assert resultado == 3


def test_potencia_2_elevado_3_igual_8():
    resultado = Calculadora().operar(Potencia(2, 3))
    assert resultado == 8


def test_raiz_cuadrada_9_igual_3():
    resultado = Calculadora().operar(RaizCuadrada(9))
    assert resultado == 3


def test_raiz_cubo_8_igual_2():
    resultado = Calculadora().operar(RaizCubo(8))
    assert resultado == 2


def test_raiz_4_de_16_igual_2():
    resultado = Calculadora().operar(Raiz(16, 4))
    assert resultado == 2


def test_con_cota_max_decorator_resultado_invalido():
    calculadora = DecoratorCotaMax(Calculadora(), 10)
    with pytest.raises(Exception) as e_info:
        calculadora.operar(Suma(7, 4))

    assert str(e_info.value) == 'resultado - Valor por encima de la cota'


def test_con_cota_max_decorator_primer_numero_invalido():
    calculadora = DecoratorCotaMax(Calculadora(), 10)
    with pytest.raises(Exception) as e_info:
        calculadora.operar(Suma(11, 4))

    assert str(e_info.value) == 'primer numero - Valor por encima de la cota'


def test_con_cota_max_decorator_segundo_numero_invalido():
    calculadora = DecoratorCotaMax(Calculadora(), 10)
    with pytest.raises(Exception) as e_info:
        calculadora.operar(Suma(4, 11))

    assert str(e_info.value) == 'segundo numero - Valor por encima de la cota'


def test_con_cota_min_decorator_segundo_numero_invalido():
    calculadora = DecoratorCotaMin(Calculadora(), 10)
    with pytest.raises(Exception) as e_info:
        calculadora.operar(Suma(11, 4))

    assert str(e_info.value) == 'segundo numero - Valor por encima de la cota'


def test_con_cota_max_y_min_decorator_anda():
    calculadora = DecoratorCotaMin(Calculadora(), 2)
    calculadora = DecoratorCotaMax(calculadora, 10)
    assert calculadora.operar(Suma(5, 4)) == 9


def test_con_cota_max_y_min_decorator_segundo_numero_invalido():
    calculadora = DecoratorCotaMin(Calculadora(), 2)
    calculadora = DecoratorCotaMax(calculadora, 10)
    with pytest.raises(Exception) as e_info:
        calculadora.operar(Suma(11, 4))

    assert str(e_info.value) == 'primer numero - Valor por encima de la cota'
