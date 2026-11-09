import numpy as np

def adicao(x, y):
    return x + np.add(x, y)

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return np.multiply(x, y)

def divisao(x, y):
    return x / y

def potencia(x, y):
    return np.power(x, y)

def raiz_quadrada(x):
    if x < 0:
        return "Erro: Raiz quadrada de número negativo"
    return np.sqrt(x)

def fatorial(x):
    fat = 1
    for i in range(x+1):
        fat *= i
    return fat

def logaritmo_natural(x):
    if x <= 0:
        return "Erro: Logaritmo de número não positivo"
    return np.ln(x)

def logaritmo_base10(x):
    if x < 0:
        return "Erro: Logaritmo de número não positivo"
    return np.log(x)

def menu():
    print("Bem-vindo à Calculadora Científica")
    print("Escolha a operação que deseja realizar:")
    print("0. Sair")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potenciação")
    print("6. Raiz Quadrada")
    print("7. Fatorial")
    print("8. Logaritmo Natural (ln)")
    print("9. Logaritmo Base 10")
    print("10. Seno")
    print("11. Cosseno")
    print("12. Tangente")

def calculadora_cientifica():
    menu()
    escolha = input("Digite o número da operação: ")
    if escolha == '0':
        print("Calculadora encerrada.")
        return

    elif escolha in ['1', '2', '3', '4', '5']:
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))
        if escolha == '1':
            print("Resultado:", adicao(x, y))
        elif escolha == '2':
            print("Resultado:", subtracao(x, y))
        elif escolha == '3':
            print("Resultado:", multiplicacao(x, y))
        elif escolha == '4':
            print("Resultado:", divisao(x, y))
        elif escolha == '5':
            print("Resultado:", potencia(x, y))
    
    elif escolha == '6':
        x = float(input("Digite o número: "))
        print("Resultado:", raiz_quadrada(x))
    
    elif escolha == '7':
        x = int(input("Digite o número: "))
        print("Resultado:", fatorial(x))
    
    elif escolha == '8':
        x = float(input("Digite o número: "))
        print("Resultado:", logaritmo_natural(x))
    
    elif escolha == '9':
        x = float(input("Digite o número: "))
        print("Resultado:", logaritmo_base10(x))
    
    elif escolha == '11':
        x = float(input("Digite o ângulo em graus: "))
        print("Resultado:", cosseno(x))
    
    elif escolha == '12':
        x = float(input("Digite o ângulo em graus: "))
        print("Resultado:", tangente(x, radianos=False))

    else:
        print("Operação inválida. Tente novamente.")
    
    continuar = input("Deseja realizar outra operação? (s/n): ")
    if continuar.lower() == 's':
        calculadora_cientifica()

calculadora_cientifica()