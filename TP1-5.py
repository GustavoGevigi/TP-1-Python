firstName = input('Insira seu primeiro nome: ')
secondName = input('Insira seu segundo nome: ')

def nameGen(firstName, secondName):
    return firstName + ' ' + secondName

print(f'Saudações {nameGen(firstName, secondName)}, é um prazer te conhecer!')