import os
import time
import operator

def calculadora(num1: float, num2: float, operador: str) -> float:
    """
    Usar nan como valor inicial é uma boa prática. 
    Se o operador fornecido não corresponder a nenhuma das opções válidas (+, -, etc.),
    a função retornará nan, sinalizando que o cálculo não pôde ser realizado.
    """
    result = float("nan")

    if operador == '+':
        result = num1 + num2
    elif operador == '-':
        result = num1 - num2
    elif operador == '*':
        result = num1 * num2
    elif operador == '/':
        if num2 == 0:
            return float("nan")
        result = num1 / num2
    elif operador == '%':
        if num2 == 0:
            return float("nan")
        result = num1 % num2
    elif operador == '^':
        result = num1 ** num2
    return result


def calculadora_v2(num1: float, num2: float, operador: str) -> float:
    if num2 == 0 and operador in ['/', '%']:
        return float("nan")

    operacoes = {
        "+": lambda: num1 + num2,
        "-": lambda: num1 - num2,
        "/": lambda: num1 / num2,
        "*": lambda: num1 * num2,
        "%": lambda: num1 % num2,
        "^": lambda: num1 ** num2,
    }
    funcao = operacoes.get(operador)
    if funcao:
        return funcao()

    return float("nan")


def calculadora_v3(num1: float, num2: float, operador: str) -> float:
    if num2 == 0 and operador in ['/', '%']:
        return float("nan")

    operadores = {
        "+": operator.add,
        "-": operator.sub,
        "/": operator.truediv,
        "*": operator.mul,
        "%": operator.mod,
        "^": operator.pow,
    }

    if operador in operadores:
        return operadores[operador](num1, num2)

    return float("nan")


# esta versão quando tentamos o expoente de 0, ela retornava um erro
def calculadora_v4(num1: float, num2: float, operador: str) -> float:
    if num2 == 0 and operador in ['/', '%']:
        return float("nan")

    operacoes = {
        "+": num1 + num2,
        "-": num1 - num2,
        "/": num1 / num2,
        "*": num1 * num2,
        "%": num1 % num2,
        "^": num1 ** num2,
    }

    return operacoes.get(operador, float("nan"))


if __name__ == "__main__":

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('Calculadora')
            print('----------------------------------\n')
            numero1: float = float(input('Introduza o primeiro número: '))
            numero2: float = float(input('Introduza o segundo número: '))
            operacao: str = input('Introduza a operação a realizar (+ - / * %) ou (^): ')
            print(f'O resultado: {calculadora(numero1, numero2, operacao)}')  # Usa versão 1 por padrão
            print()
            cont: str = input('Deseja continuar? (s/n): ').lower()
            if cont == 'n':
                break

        except ValueError:
            print('Dados inválidos! -> Tente novamente!')
            time.sleep(2)

        except ZeroDivisionError:
            print('Impossível dividir por zero! -> Tente novamente!')
            time.sleep(2)

    print('\nVolte sempre!\n')
