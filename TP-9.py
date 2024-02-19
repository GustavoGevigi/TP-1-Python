import random

def discountCalc(userPrice, userDiscount):
    discount = (userDiscount / 100) * userPrice
    discountValue = userPrice - discount
    return discountValue

userPrice = random.randint(100, 200)
userDiscount = 0
print(f"Valor de produto: {userPrice}")

if userPrice >= 100:
    userDiscount = 10
    print(f"Valor com desconto de 10%: {discountCalc(userPrice, userDiscount)}")
elif userPrice >= 200:
    userDiscount = 15
    print(f"Valor com desconto de 15%: {discountCalc(userPrice, userDiscount)}")
