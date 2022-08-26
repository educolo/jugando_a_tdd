from abc import ABC, abstractmethod


class PersonaConSueldo(ABC):
    def __init__(self, nombre, sueldo):
        self.__nombre = nombre
        self.__sueldo = sueldo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def sueldo(self):
        return self.__sueldo

    @abstractmethod
    def calcular_presupuesto(self):
        pass


class Empleada(PersonaConSueldo):

    def calcular_presupuesto(self):
        return self.sueldo


class Jefa(PersonaConSueldo):

    def __init__(self, *args, **kwargs):
        self.__empleadas = []
        super(Jefa, self).__init__(*args, **kwargs)

    def calcular_presupuesto(self):
        presupuesto = 0
        for empleada in self.empleadas:
            presupuesto += empleada.calcular_presupuesto()

        presupuesto += self.sueldo

        return presupuesto

    def agregar_empleada(self, empleada):
        try:
            empleada.calcular_presupuesto
        except:
            raise Exception('Necesita usar una persona con sueldo')
        
        self.empleadas.append(empleada)

    @property
    def empleadas(self):
        return self.__empleadas
