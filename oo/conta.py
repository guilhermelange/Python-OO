class Conta:
    codigos_bancos = {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

    def __init__(self, numero, titular, saldo, limite=1000.0):
        print("Contruindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_sacar):
        valor_disponivel_sacar = self.__saldo + self.limite
        return valor_sacar <= valor_disponivel_sacar

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def set_limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"
