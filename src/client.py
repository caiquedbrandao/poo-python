import datetime
from src import utils

# just a text


class Client:

    __slots__ = ['_name', '_last_name', '_cpf', '_birth_date']

    def __init__(self, name, last_name, cpf, birth_date):
        self._name = name
        self._last_name = last_name
        self._cpf = cpf
        self._birth_date = datetime.datetime.strptime(
            birth_date, '%d/%m/%Y').date()

    def __str__(self):
        return "Nome: {} | CPF {}".format(self._name, self._cpf)


if __name__ == '__main__':

    cliente1 = Client('Caíque', 'Brandão', '10483042641', '15/09/1994')
    print(cliente1)
    print(cliente1._birth_date)
    print(type(cliente1._birth_date))
