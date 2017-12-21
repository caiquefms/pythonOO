class Conta:
    def __init__(self,numero,titular,saldo,limite = 1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print("Saldo {0} do titular {1}".format(self.__saldo,self.__titular))

    def deposita(self,valor):
        self.__saldo += valor

    def saca(self,valor):
        self.__saldo -= valor

    def transfere(self,valor,destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self,limite):
        self.__limite = limite
