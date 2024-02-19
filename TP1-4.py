def userNumInput():
    userIpt1 = int(input("Insira seu primeiro número: "))
    userIpt2 = int(input("Insira seu segundo número: "))
    return userIpt1, userIpt2

def returnMenu():
    returnInpt = int(input('Pressione 0 retornar ao menu: '))
    match returnInpt:
        case 0:
            menuGenerator()


def sumFunc():
    num1, num2 = userNumInput()
    result = num1 + num2
    print(f'A soma é: {result}')
    returnMenu()

def subFunc():
    num1, num2 = userNumInput()
    result = num1 - num2
    print(f'A subtração é: {result}')
    returnMenu()

def mulFunc():
    num1, num2 = userNumInput()
    result = num1 * num2
    print(f'A multiplicação é: {result}')
    returnMenu()

def divFunc():
    num1, num2 = userNumInput()
    result = num1 / num2
    print(f'A divisão é: {result}')
    returnMenu()

def menuGenerator():
    print("""
    Escolha uma das operações disponíveis:
    
    [1] Somar
    [2] Subtrair
    [3] Multiplicar
    [4] Divisao
    [0] Sair do Programa
    """)

    option = int(input("Digite a operação desejada: "))
    operations = {
        0 : exit(),
        1 : sumFunc,
        2 : subFunc,
        3 : mulFunc,
        4 : divFunc,
    }

    if option in operations:
        operations[option]()
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

menuGenerator()