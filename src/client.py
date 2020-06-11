import datetime
from src import utils

class Cliente:

    def __init__(self, nome, sobrenome, cpf, data_nascimento):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf
        self._data_nascimento = datetime.datetime.strptime(data_nascimento, '%d/%m/%Y').date()

    def __str__(self):
        return "Nome: {} | CPF {}".format(self._nome, self._cpf)


if __name__ == '__main__':

    cliente1 = Cliente('Caíque', 'Brandão', '10483042641', '15/09/1994')
    print(cliente1)
    print(cliente1._data_nascimento)
    print(type(cliente1._data_nascimento))

