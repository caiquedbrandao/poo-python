import datetime
from src import bank, account, client, account_updater

if __name__ == '__main__':

    banc1 = bank.Bank('Picpay', '19547148412')

    print(banc1)
    print(banc1._created_at)
    print(banc1.created_at)
    print(banc1.updated_at)
    print(datetime.datetime.now())

    cliente1 = client.Client('Caíque', 'Brandão', '10483042641', '15/09/1994')
    cliente2 = client.Client('Thainá', 'Brandão', '41970143843', '21/05/1995')
    cliente3 = client.Client('João', 'Brandão', '41970143843', '21/05/1995')

    #c = Conta('123-4', cliente1, 1000.0)
    cc1 = account.CurrentAccount(cliente1, 750.0)
    cc2 = account.CurrentAccount(cliente2, 1750.0)
    #cp = ContaPoupanca('123-6', cliente3, 1000.0)

    #cc.atualiza(0.2)
    #ci.atualiza(0.2)


    #banc1.adicionaConta(c)
    banc1.addAccount(cc1)
    banc1.addAccount(cc2)
    #banc1.adicionaConta(cp)
    #banc1.adicionaConta(c2)
    #banc1.adicionaConta(ci)

    print(banc1)

    adc = account_updater.AccountUpdater(0.04)

    for c in banc1.accounts:
        adc.update(c)

    print('Saldo total: {}'.format(adc.total_balance))

    print(account.Account.getAccountsTotal())