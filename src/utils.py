import datetime

class Mydate:

    def __init__(self):
        date = datetime.datetime.today()
        self.year = date.year
        self.month = date.month
        self.day = date.day

class AutenticavelMixIn:

    def autentica(self, password):
        if self._password == password:
            print("acesso permitido")
            return True
        else:
            print("acesso negado")
            return False
        
class AtendimentoMixIn:
    def cadastra_atendimento(self):
        print('# faz cadastro atendimento')

    def atende_cliente(self):
        print('# faz atendimento')

class HoraExtraMixIn:

    def calcula_hora_extra(self, horas):
        print('# calcula horas extras')