class Conta:
    def __init__(self,numero,titular,saldo,limite = 1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


    def extrato(self):
        print("Saldo {0} do titular {1}".format(self.saldo,self.titular))

    def deposita(self,valor):
        self.saldo += valor

    def saca(self,valor):
        self.saldo -= valor