from gerente import funcoesgerente
from gerente.telas import imprimir
from gerente import traduzir

def auterar(tipo):
    while True:
        email = input(traduzir.traduzir("Informe o E-mail do {}: ", tipo))
        email2 = input(traduzir.traduzir("Informe o novo E-mail: "))
        if funcoesgerente.auterarEmail(email, tipo, email2) != "":
            print(traduzir.traduzir("E-mail auterado com sucesso!"))
            break
        print(traduzir.traduzir("Esse E-mail não existe"))