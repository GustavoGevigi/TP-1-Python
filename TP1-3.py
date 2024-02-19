firstName = input('Insira seu primeiro nome: ')
secondName = input('Insira seu segundo nome: ')

def nameGen(firstName, secondName):
    return firstName + ' ' + secondName

print(f'O nome inteiro digitado é: {nameGen(firstName, secondName)}')