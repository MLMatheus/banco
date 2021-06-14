from gerente import funcoesgerente
from gerente.telas import imprimir
from gerente import traduzir

def auterar(tipo):
    while True:
        email = input(traduzir.traduzir("Informe o E-mail do {}: ", tipo))
        if tipo == "gerente":
            while True:
                senha = input(traduzir.traduzir("Informe a senha de acesso: "))
                senha2 = input(traduzir.traduzir("Repita a senha digitada anteriormente: "))
                if senha == senha2:
                    break
                print(traduzir.traduzir("As senhas digitadas não são iguais"))
        else:
            senha = ""
        dados = funcoesgerente.auterarSenha(email, tipo, senha)
        if dados != "":
            if tipo == "cliente":
                print(traduzir.traduzir(dados))
                break
            print(traduzir.traduzir("Senha auterada com sucesso!"))
            break
        print(traduzir.traduzir("Esse E-mail não existe"))