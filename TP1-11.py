import random

userInput = int(input("Escolha quantos dados jogar: "))
diceOrder = 1
def diceGame():
    diceResult = random.randint(1, 6)
    print(f"Dado {diceOrder}: {diceResult}")

contador = 0
while contador < userInput:
    diceGame()
    diceOrder += 1
    contador += 1