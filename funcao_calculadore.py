def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2  # Soma
    elif operacao == 2:
        return num1 - num2  # Subtração
    elif operacao == 3:
        return num1 * num2  # Multiplicação
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2  # Divisão
        else:
            return "Erro: Divisão por zero"
    else:
        return 0  # Operação inválida

# Exemplo de uso
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = int(input("Escolha a operação (1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão): "))

resultado = calculadora(num1, num2, operacao)
print(f"Resultado: {resultado}")
