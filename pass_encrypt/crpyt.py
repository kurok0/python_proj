import bcrypt

passwd_Master = input("Insira a senha-mestre: ")
senha = "tsBG0Ud^ZDwootIx@=x-"
if passwd_Master == senha:
    def view():
        with open('pass.txt', 'r') as f:
            for f in f.readlines():
                data = f.rstrip()
                usr, passw = data.split("|")
                print("User:", usr, ">>" ,"Password:", passw)
    def add():
        user = input("Insira seu usuário: ")
        passwd = input("Insira sua senha: ")
        crpt_pass = bcrypt.hashpw(passwd.encode('utf8'), bcrypt.gensalt())

        with open('pass.txt', 'a') as f:
            f.write(user + "|" + str(crpt_pass) + "\n")

    while(True):
        print("Caso queira sair, pressione q + enter")
        option = input("Você gostaria de add ou view Usuários e Senhas? ")
        if option == 'q':
            break
        elif option == 'add':
            add()
        elif option == 'view':
            view()

        else:
            print("Comando Inválido.")
            continue
else:
    print("Senha-mestre incorreta.")