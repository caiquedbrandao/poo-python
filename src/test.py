import datetime
from src import bank, account

if __name__ == '__main__':

    banc1 = bank.Bank('Picpay', '19547148412')

    print(banc1)
    print(banc1._created_at)
    print(banc1.created_at)
    print(banc1.updated_at)
    print(datetime.datetime.now())