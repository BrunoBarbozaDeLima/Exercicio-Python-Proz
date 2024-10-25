# Exercicio-Python-Proz
 Exercicio Python Proz

# Calculadora Simples

Este projeto implementa uma função calculadora em Python que realiza quatro operações básicas: soma, subtração, multiplicação e divisão. A função recebe dois números e um código de operação, executando a operação correspondente com base nos parâmetros fornecidos.

## Funcionalidades

A calculadora suporta as seguintes operações:

1. **Soma**: Retorna a soma de dois números.
2. **Subtração**: Retorna a subtração do segundo número do primeiro.
3. **Multiplicação**: Retorna o produto dos dois números.
4. **Divisão**: Retorna o quociente da divisão do primeiro número pelo segundo, verificando se o divisor é diferente de zero.

Caso o usuário insira um código de operação inválido (fora de 1 a 4), a função retornará `0` como resultado padrão.

## Exemplo de Código

```python
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
