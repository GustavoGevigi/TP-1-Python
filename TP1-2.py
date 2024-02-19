userInput = int(input(f'Insira a quantidade de minutos: '))

convertedHours = userInput // 60
convertedMinutes = userInput % 60

print(f'{userInput} minutos é igual a {convertedHours} horas e {convertedMinutes} minutos')