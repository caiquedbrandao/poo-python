import datetime
from src import utils, client, account_updater
from abc import ABC, abstractmethod

class Account(ABC):

    _accounts_id = 0
    _accounts_number = 1000

    @classmethod
    def getAccountsTotal(cls):
        return cls._accounts_id

    @classmethod
    def updateAccountsId(cls):
        cls._accounts_id += 1

    @classmethod
    def updateAccountsNumber(cls):
        cls._accounts_number += 1

    __slots__ = ['_id', '_created_at', '_number', '_holder', '_balance', '_limit', '_historic']

    def __init__(self, client, balance=0, limit=1000.0):
        now = datetime.datetime.now()
        self._id = type(self)._accounts_id + 1
        self._created_at = now
        self._number = type(self)._accounts_number + 1
        self._holder = client
        self._balance = balance
        self._limit = limit
        self._historic = Historic(now)
        type(self).updateAccountsId()
        type(self).updateAccountsNumber()

    @property
    def balance(self):
        return self._balance

    @abstractmethod
    def update(self, rate):
        self._balance += self._balance * rate

    def deposit(self, amount):
        self._balance += amount
        self._historic.transactions.append("deposit: {:.2f}".format(amount))

    def withdraw(self, amount):
        if (self._balance < (amount + self._limit)):
            return False
        else:
            self._balance -= amount
            self._historic.transactions.append("withdraw: {:.2f}".format(amount))
            return True

    def transferTo(self, destination, amount):
        withdrew = self.withdraw(amount)
        if (withdrew == False):
            return False
        else:
            destination.deposit(amount)
            self._historic.transactions.append("transfer of {:.2f} to account {}".format(amount, destination._number))
            return True

    def statement(self):
        print("Id: {} | Account: {} | Created at: {:4}-{:02}-{:02} | CPF: {} | Name: {} {} | Balance: {:.2f}".format(
            self._id, self._number, self._created_at.year, self._created_at.month, self._created_at.day,
            self._holder._cpf, self._holder._name, self._holder._last_name, self._balance
        ))
        self._historic.transactions.append("took extract - balance of {}".format(self._balance))

    def __str__(self):
        return "id: {} | Account Number: {} | Created at: {:4}-{:02}-{:02}".format(
            self._id, self._number, self._created_at.year, self._created_at.month, self._created_at.day
        )

class Historic:
    def __init__(self, created_at):
        self.created_at = created_at
        self.transactions = ["Account oppened - date: {}".format(created_at)]

    def prints(self):
        print("=" * 50)
        print("Created at: {}".format(self.created_at))
        print("\nTransactions: ")
        [print("-", t) for t in self.transactions]

class CurrentAccount(Account):
    def __init__(self, holder, balance=0, limit=0):
        super().__init__(holder, balance, limit)
        self._type = 'conta_corrente'
        self._id = Account._accounts_id + 1
        Account.updateAccountsId()
        Account.updateAccountsNumber()

    def update(self, rate):
        self._balance += self._balance * (rate * 2)

    def __str__(self):
        return "Account type: {} | Id: {} | Account number: {} | Created at: {:4}-{:02}-{:02} | cpf: {}".format(
            self._type, self._id, self._number, self._created_at.year,
            self._created_at.month, self._created_at.day, self._holder._cpf
        )