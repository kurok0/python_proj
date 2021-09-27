def repetir():

    while True:
        a = [""]
        a.append((input("Nome da instituição ou de sua preferência: ")))
        a = list(set(a))
        choice = input("Pressione q + enter para sair, para continuar pressione enter: ")
        if(choice == "q"):
                break
        else:
                print(a)
                print("Continuando...")