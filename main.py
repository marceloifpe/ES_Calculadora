class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def somar(self):
        return self.a + self.b

    def multiplicar(self):
        return self.a * self.b

    def subtrair(self):
        return self.a - self.b

    def dividir(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Erro: Divisão por zero não é permitida."


while True:
    try:
        operacao = int(input(
            "Selecione a operação desejada na Calculadora (1 -> soma, 2 -> Subtração, 3 -> multiplicação, 4 -> divisão): "))

        if operacao not in [1, 2, 3, 4]:
            raise ValueError(
                "Operação inválida. Por favor, selecione uma operação válida.")
    except ValueError as e:
        print(e)
        continue

    if operacao == 1:
        numeros = input(
            "Digite os números que deseja somar, separados por '+': ")
        numeros = [float(n) for n in numeros.split('+')]
        resultado = Calculadora(*numeros).somar()
        print(f"O resultado da operação de soma é = {resultado}")
    elif operacao == 2:
        numeros = input(
            "Digite os números que deseja subtrair, separados por '-': ")
        numeros = [float(n) for n in numeros.split('-')]
        resultado = Calculadora(*numeros).subtrair()
        print(f"O resultado da operação de subtração é = {resultado}")
    elif operacao == 3:
        numeros = input(
            "Digite os números que deseja multiplicar, separados por '*': ")
        numeros = [float(n) for n in numeros.split('*')]
        resultado = Calculadora(*numeros).multiplicar()
        print(f"O resultado da operação de multiplicação é = {resultado}")
    elif operacao == 4:
        numeros = input(
            "Digite os números que deseja dividir, separados por '/': ")
        numeros = [float(n) for n in numeros.split('/')]
        resultado = Calculadora(*numeros).dividir()
        if isinstance(resultado, str):
            print(resultado)
        else:
            print(f"O resultado da operação de divisão é = {resultado}")
    break
