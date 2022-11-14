class Conta:
    def __init__(self, agencia, saldo = 0, ):
        self._saldo = saldo
        self.agencia = agencia
    
    def depositar(self, valor):
        self._saldo += valor
        print(f"Valor depositado: {valor}.")

    def sacar(self, valor):
        self._saldo -= valor
        print(f"Valor Sacado: {valor}. Saldo:")

    def mostrarSaldo(self, saldo):
        return self._saldo


conta = Conta(100)
print(conta._saldo)

conta.depositar(50)
print(conta._saldo)
print(conta.agencia)
print(conta._saldo)
