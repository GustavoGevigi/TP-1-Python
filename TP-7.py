userHeight = float(input("Digite sua altura: "))
userWeight = float(input("Digite seu peso: "))

def imcCalc(userHeight, userWeight):
    imc = userWeight / (userHeight * userHeight)
    return imc

imcResult = imcCalc(userHeight, userWeight)
if imcResult < 18.5:
    print("Abaixo do peso")
elif imcResult >= 18.5 and imcResult < 25:
    print("Peso normal")
elif imcResult >= 25 and imcResult < 30:
    print("Sobrepeso")
elif imcResult >= 30 and imcResult < 39:
    print("Obesidade")
elif imcResult >= 39:
    print("Obesidade Grave")