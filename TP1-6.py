import random

sortedNum  = random.randint(1, 10)


while True:
    userInput = int(input('Digite um número: '))

    if userInput < sortedNum:
        print('Muito baixo! Tente novamente.')
    elif userInput > sortedNum:
        print('Muito alto! Tente novamente.')
    else:
        print(f'Parabéns! O número sortido é {sortedNum}')
        break
