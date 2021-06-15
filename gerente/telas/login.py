from gerente import funcoesgerente
from gerente import traduzir
from gerente.telas import imprimir

def login():
    while True:
        email = input(traduzir.traduzir("Informe seu E-mail: "))
        senha = input(traduzir.traduzir("Informe sua senha: "))
        if funcoesgerente.fazerLogin(email, senha):
            print(traduzir.traduzir("Logado com sucesso!"))
            break
        print(traduzir.traduzir("E-mail ou senha incorretos"))