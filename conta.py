class Conta:
    def __init__(self, numero, titulo, saldo, limite):
        print(f"Construindo objeto... {self}")
        self.__numero = numero
        self.__titulo = titulo
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca (self, valor):
        if(self.pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou do limite")

    def transfere(self, valor, origem, destino):
        origem.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

