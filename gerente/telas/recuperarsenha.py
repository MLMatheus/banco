from gerente import funcoesgerente
from gerente.telas import imprimir
from gerente import traduzir

def recuperar(tipo):
    while True:
        email = input(traduzir.traduzir("Informe o E-mail do {}: ", tipo))
        if funcoesgerente.recuperarSenha(email, tipo) != "":
            print(traduzir.traduzir(funcoesgerente.recuperarSenha(email, tipo)))
            break
        print(traduzir.traduzir("Esse E-mail não existe"))