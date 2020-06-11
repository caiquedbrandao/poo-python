from abc import ABC, abstractmethod
from src import utils

class Employee(ABC):

    __slots__ = ['_name', '_cpf', '_salary']

    def __init__(self, name, cpf, salary=0):
        self._name = name
        self._cpf = cpf
        self._salary = salary

    @abstractmethod
    def get_bonus(self):
        return self._salary * 0.15

class Leadership(Employee):

    __slots__ = ['_password', '_subordinates']

    def __init__(self, name, cpf, salary, password, subordinates):
        super().__init__(name, cpf, salary)
        self._password = password
        self._subordinates = subordinates


class Manager(Leadership, utils.AutenticavelMixIn, utils.HoraExtraMixIn):

    __slots__ = ['_postion']

    def __init__(self, name, cpf, salary, password, subordinates, position='Manager'):
        super().__init__(name, cpf, salary, password, subordinates)
        self._postion = position

    @property
    def position(self):
        return self._postion

    def get_bonus(self):
        return self._salary * 0.15 + 1000

    def __str__(self):
        return '< Instance de {}; address:{}>'.format(self.__class__.__name__, id(self))


class Director(Leadership, utils.AutenticavelMixIn):

    __slots__ = ['_postion']

    def __init__(self, name, cpf, salary, password, subordinates, position='Director'):
        super().__init__(name, cpf, salary, password, subordinates)
        self._postion = position

    @property
    def position(self):
        return self._postion

    def get_bonus(self):
        return super().get_bonus() * 1.5

    def __str__(self):
        return '< Instance of {}; address:{}>'.format(self.__class__.__name__, id(self))

class Clerk(Employee, utils.AtendimentoMixIn):
    pass

class BonusControl:

    def __init__(self, total_bonus=0):
        self._total_bonus = total_bonus

    def register(self, obj):

        if(hasattr(obj, 'get_bonus')):
            self._total_bonus += obj.get_bonus()
        else:
            print("'Instance of {} do not implements the method get_bonus().".format(self.__class__.__name__))

    @property
    def total_bonus(self):
        return self._total_bonus

"""
if __name__ == '__main__':
    #funcionario = Funcionario('João', '111111111-11', 2000.0)
    #print("bonificacao funcionario: {}".format(funcionario.get_bonificacao()))

    gerente = Manager("José", "222222222-22", 7000.0, '1234', 4)
    print(gerente)
    print("bonificacao gerente: {}".format(gerente.get_bonus()))
    gerente.autentica('123')

    diretor = Director('joao', '111111111-11', 4000.0, '1234', 2)
    print(diretor)
    print("bonificacao diretor: {}".format(diretor.get_bonus()))
    gerente.autentica('1234')

    controle = BonusControl()
    controle.register(gerente)
    controle.register(diretor)
    print("total: {}".format(controle.total_bonus))
"""