from .operacion import Operacion


class CalculadoraBase:
    def __init__(self, logger=None):
        self.__logger = logger

    @property
    def logger(self):
        return self.__logger

    def operar(self, operacion):
        raise NotImplementedError()


class Calculadora(CalculadoraBase):
    def operar(self, operacion):
        if self.logger is not None:
            self.logger.log(operacion)
        return operacion.ejecutar()


class DecoratorCotaBase(CalculadoraBase):
    def __init__(self, calculadora, cota):
        self.__calculadora = calculadora
        self.__cota = cota

    @property
    def calculadora(self):
        return self.__calculadora

    @property
    def cota(self):
        return self.__cota

    def validar_parametro(self, valor, parametro=''):
        raise NotImplementedError()

    def operar(self, operacion):
        self.validar_parametro(operacion.primer_numero, 'primer numero')
        self.validar_parametro(operacion.segundo_numero, 'segundo numero')
        resultado = self.calculadora.operar(operacion)
        self.validar_parametro(resultado, 'resultado')
        return resultado


class DecoratorCotaMax(DecoratorCotaBase):
    def validar_parametro(self, valor, parametro=''):
        if valor > self.cota:
            raise Exception(f'{parametro} - Valor por encima de la cota')


class DecoratorCotaMin(DecoratorCotaBase):
    def validar_parametro(self, valor, parametro=''):
        if valor < self.cota:
            raise Exception(f'{parametro} - Valor por encima de la cota')


class Suma(Operacion):
    def ejecutar(self):
        return self.primer_numero + self.segundo_numero


class Resta(Operacion):
    def ejecutar(self):
        return self.primer_numero - self.segundo_numero


class Multiplicacion(Operacion):
    def ejecutar(self):
        return self.primer_numero * self.segundo_numero


class Division(Operacion):
    def ejecutar(self):
        return self.primer_numero / self.segundo_numero


class Potencia(Operacion):
    def ejecutar(self):
        return self.primer_numero ** self.segundo_numero


class Raiz(Operacion):
    def ejecutar(self):
        return self.primer_numero ** (1 / self.segundo_numero)


class RaizCuadrada(Raiz):
    def __init__(self, primer_numero):
        super().__init__(primer_numero, 2)


class RaizCubo(Raiz):
    def __init__(self, primer_numero):
        super().__init__(primer_numero, 3)
