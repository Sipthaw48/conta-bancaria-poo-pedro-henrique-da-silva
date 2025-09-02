class ContaBancaria:
    def __init__(self, titular: str):
        self.titular = titular
        self.saldo = 2014.52

    def exibir_saldo(self):
        print(f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}")


if __name__ == "__main__":
    conta = ContaBancaria("Maria")
    conta.exibir_saldo()
