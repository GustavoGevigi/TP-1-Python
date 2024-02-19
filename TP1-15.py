def interactiveStory():
    print("Bem-vindo à História Interativa!")

    choice1 = input("Você deseja entrar na floresta? (sim/não): ").lower()

    if choice1 == "sim":
        choice2 = input("Você encontra uma bifurcação. Você quer ir para a esquerda ou para a direita? (esquerda/direita): ").lower()

        if choice2 == "esquerda":
            print("Você descobre um tesouro escondido! Parabéns, você é rico!")
        elif choice2 == "direita":
            print("Você se perde na floresta. Parece que você precisa de um mapa.")
        else:
            print("Escolha inválida. Reinicie a história.")
    elif choice1 == "não":
        print("Você decide não entrar na floresta. A história termina aqui.")
    else:
        print("Escolha inválida. Reinicie a história.")

interactiveStory()
