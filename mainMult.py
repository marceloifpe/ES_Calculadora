class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def multiplicar(self):
        return self.a * self.b

while True:
    print("0. Sair")
    print("1. Multiplicação")

    opcao = int(input("Opção: "))

    if opcao == 0:
        break
    elif opcao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        c = Calculadora(num1, num2)
        print("Resultado da multiplicação:", c.multiplicar())
    else:
        print("Opção inválida. Tente novamente.")
