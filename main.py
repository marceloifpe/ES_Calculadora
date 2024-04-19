class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def somar(self):
        return self.a + self.b


    def multiplicar(self):
        return self.a * self.b

while True:
    try:
        operacao = int(input("Selecione a operação desejada na Calculadora (1 para soma, 2 para multiplicação): "))

        if operacao not in [1, 2]:
            raise ValueError("Operação inválida. Por favor, selecione uma operação válida.")
    except ValueError as e:
        print(e)
        continue

    if operacao == 1:
        numeros = input("Digite os números que deseja somar, separados por '+': ")
        numeros = [float(n) for n in numeros.split('+')]
        resultado = Calculadora(*numeros).somar()
        print(f"O resultado da operação de soma é = {resultado}")
    elif operacao == 2:
        numeros = input("Digite os números que deseja multiplicar, separados por '*': ")
        numeros = [float(n) for n in numeros.split('*')]
        resultado = Calculadora(*numeros).multiplicar()
        print(f"O resultado da operação de multiplicação é = {resultado}")
    break