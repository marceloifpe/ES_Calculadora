def soma(*numeros):
    return sum(numeros)

while True:
    try:
        # 1 para soma, 2 para subtração, 3 para multiplicação e 4 para divisão.
        operacao = int(input("Selecione a operação desejada na Calculadora: "))
        
        if operacao not in [1, 2, 3, 4]:
            raise ValueError("Operação inválida. Por favor, selecione uma operação válida.")
    except ValueError as e:
        print(e)
        continue

    if operacao == 1:
        numeros = input("Digite os números que deseja somar, separados por '+': ")
        numeros = [float(n) for n in numeros.split('+')]
        resultado = soma(*numeros)
        print(f"O resultado da operação de soma é = {resultado}")
    break
