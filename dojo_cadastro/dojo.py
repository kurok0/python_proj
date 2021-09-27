import getpass
from os import name
import pyodbc

cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=127.0.0.1\mssqlserver2008;"
                      "Database=prog;"
                      "Trusted_Connection=yes;")
cursor = cnxn.cursor()

nameinput = input("Insira seu nome:\n")
mailinput = input("Insira seu email:\n")
with open("email", "r") as f:
    for l_num, l in enumerate(f, 1):
        if (mailinput in l):
            raise NameError("Este e-mail já existe.")
with open("email", "a") as mail:
    mail.write("***" + mailinput)
userinput = input("Insira seu usuário:\n")
with open("user", "r") as sf:
    for l_num, l in enumerate(sf, 1):
        if (userinput in l):
            print('Sugestão de usuários:')
            print(userinput[:2] + mailinput[:6])
            print(userinput[:4] + mailinput[:3])
            print(userinput[:6] + mailinput[:5])
            raise NameError("Este e-mail já existe.")
with open("user", "a") as user:
    user.write("***" + userinput)
if(userinput == mail):
    raise NameError("Este usuário já existe.")
mypass = getpass.getpass("Insira sua senha:\n")
print('Cadastro realizado com sucesso!')

cursor.execute(
'INSERT INTO prog.dbo.dojo(name, email, usr, passwd) VALUES(?, ?, ?, ?)', (nameinput, mailinput, userinput, mypass))
cnxn.commit()
