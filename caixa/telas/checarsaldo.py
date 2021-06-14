from caixa import funcoescaixa
from caixa import traduzir

def checarSaldo():
    while True:
        conta = input(traduzir.traduzir("Informe o número da conta: "))
        senha = input(traduzir.traduzir("Informe sua senha numérica de 6 dígitos: "))
        saldo = funcoescaixa.checarSaldo(conta, senha)
        if saldo != -1:
            print(traduzir.traduzir("Saldo total em conta: {}", saldo))
            break
        print(traduzir.traduzir("Conta ou senha incorretas"))