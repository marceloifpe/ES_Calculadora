def soma(*numeros):
    return sum(numeros)


def subtrair(*numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado -= num
    return resultado


def multiplicar(*numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado *= num
    return resultado


def divisao(numerador, denominador):
    if denominador == 0:
        raise ValueError("Erro: Divisão por zero não é permitida.")
    return numerador / denominador


while True:
    try:
        # 1 para soma, 2 para subtração, 3 para multiplicação e 4 para divisão.
        operacao = int(input("Selecione a operação desejada na Calculadora: "))

        if operacao not in [1, 2, 3, 4]:
            raise ValueError(
                "Operação inválida. Por favor, selecione uma operação válida.")

        if operacao == 1:
            numeros = input(
                "Digite os números que deseja somar, separados por '+': ")
            numeros = [float(n) for n in numeros.split('+')]
            resultado = soma(*numeros)
            print(f"O resultado da operação de soma é = {resultado}")
        elif operacao == 2:
            numeros = input(
                "Digite os números que deseja subtrair, separados por '-': ")
            numeros = [float(n) for n in numeros.split('-')]
            resultado = subtrair(*numeros)
            print(f"O resultado da operação de subtração é = {resultado}")
        elif operacao == 3:
            numeros = input(
                "Digite os números que deseja multiplicar, separados por '*': ")
            numeros = [float(n) for n in numeros.split('*')]
            resultado = multiplicar(*numeros)
            print(f"O resultado da operação de multiplicação é = {resultado}")
        elif operacao == 4:
            numerador = float(input("Digite o numerador para a divisão: "))
            denominador = float(input("Digite o denominador para a divisão: "))
            try:
                resultado = divisao(numerador, denominador)
                print(f"O resultado da operação de divisão é = {resultado}")
            except ValueError as e:
                print(e)
        break
    except ValueError as e:
        print(e)
