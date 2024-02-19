userInput = input("Insira uma palavra: ")

def palindrome(text):
    formatedText = text.replace(" ", "").lower()
    return formatedText == formatedText[::-1]

if palindrome(userInput):
    print(f"{userInput} é Palindromo")
else:
    print(f"{userInput} não é Palindromo")