import datetime

class Bank:
    def __init__(self, name, cnpj, accounts=[]):
        now = datetime.datetime.now()
        self._name = name
        self._cnpj = cnpj
        self._accounts = accounts
        self._created_at = now
        self._updated_at = now

    @property
    def name(self):
        return self._name

    @property
    def cnpj(self):
        return self._cnpj

    @property
    def accounts(self):
        return self._accounts

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at

    def addAccount(self, account):
        self._accounts.append(account)

    def getAccount(self, account):
        self._accounts.index(account)

    def getAccountsTotal(self):
        return len(self._accounts)

    def __str__(self):
        return "Bank: {} | CNPJ: {} | Accounts opened: {}".format(self._name, self._cnpj, self.getAccountsTotal())