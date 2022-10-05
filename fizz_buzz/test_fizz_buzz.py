from .main import fizz_buzz


def test_fizz_buzz_devuelve_fizz_para_multiplo_3():
    resultado = fizz_buzz(3)
    assert resultado == 'fizz'


def test_fizz_buzz_devuelve_fizz_para_multiplo_3_2():
    resultado = fizz_buzz(6)
    assert resultado == 'fizz'


def test_fizz_buzz_devuelve_buzz_para_multiplo_5():
    resultado = fizz_buzz(5)
    assert resultado == 'buzz'


def test_fizz_buzz_devuelve_fizzBuzz_para_multiplo_3_y_5():
    resultado = fizz_buzz(15)
    assert resultado == 'fizzBuzz'
