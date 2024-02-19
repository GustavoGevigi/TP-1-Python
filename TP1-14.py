def votation():
    options = ["Opcao A", "Opcao B", "Opcao C"]
    votes = [0, 0, 0]

    print("Votação - Escolha uma opção:")
    for i, opcao in enumerate(options, 1):
        print(f"[{i}] {opcao}")

    num_votes = int(input("Digite o número da opção desejada (ou 0 para encerrar a votação): "))

    while num_votes != 0:
        if 1 <= num_votes <= len(options):
            votes[num_votes - 1] += 1
            print(f"Voto registrado para {options[num_votes - 1]}!")
        else:
            print("Opção inválida. Tente novamente.")

        num_votes = int(input("Digite o número da opção desejada (ou 0 para encerrar a votação): "))

    print("\nResultado da votação:")
    for i, opcao in enumerate(options):
        print(f"{opcao}: {votes[i]} votos")

votation()
