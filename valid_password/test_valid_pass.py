from .main import (
    valid_pass,
    validar_longitud,
    validar_dos_numeros,
    validar_mayusculas,
    validar_caracter_especial,
)


def test_valid_pass_menos_8_caracteres_devuelve_false():
    resultado = valid_pass('A$34567')
    assert resultado == (False, 'La password debe contener al menos 8 caracteres')


def test_valid_pass_devuelve_true():
    resultado = valid_pass('A$#345678')
    assert resultado is True


def test_valid_pass_sin_numeros_devuelve_false():
    resultado = valid_pass('A$cdefghijk')
    assert resultado == (False, 'La password debe contener al menos 2 números')


def test_valid_pass_devuelve_multiples_errores():
    resultado = valid_pass('mipass')
    assert resultado == (False, 'La password debe contener al menos 8 caracteres\nLa password debe contener al menos 2 números\nLa password debe contener al menos una letra mayúscula\nLa password debe contener al menos un caracter especial')


def test_valid_pass__no_contiene_mayusculas_devuelve_false():
    resultado = valid_pass('$bcdefghijk123')
    assert resultado == (False, 'La password debe contener al menos una letra mayúscula')


def test_valid_pass_no_contiene_caracter_especial_false():
    resultado = valid_pass('Abcdefghijk123')
    assert resultado == (False, 'La password debe contener al menos un caracter especial')


def test_validar_longitud_false():
    assert validar_longitud('12345') is False


def test_validar_longitud_false():
    assert validar_longitud('123456789') is True


def test_validar_dos_numeros_true():
    assert validar_dos_numeros('123456') is True


def test_validar_dos_numeros_false():
    assert validar_dos_numeros('abcde') is False


def test_validar_mayusculas_true():
    assert validar_mayusculas('Abc') is True


def test_validar_mayusculas_false():
    assert validar_mayusculas('abc') is False


def test_validar_caracter_especial_true():
    assert validar_caracter_especial('$%') is True


def test_validar_caracter_especial_false():
    assert validar_caracter_especial('abc123') is False
