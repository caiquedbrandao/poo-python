from abc import ABC, abstractmethod

class AccountUpdater(ABC):
    def __init__(self, selic, total_balance=0):
        self._selic = selic
        self._total_balance = total_balance

    @property
    def selic(self):
        return self._selic

    @property
    def total_balance(self):
        return self._total_balance

    def update(self, account):
        account.statement()
        account.update(self._selic)
        self._total_balance = account.balance
        account.statement()
