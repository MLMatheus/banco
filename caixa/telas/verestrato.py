from caixa import funcoescaixa
from caixa import traduzir

def verEstrato():
    while True:
        conta = input(traduzir.traduzir("Informe o número da conta: "))
        senha = input(traduzir.traduzir("Informe sua senha numérica de 6 dígitos: "))
        estratos = funcoescaixa.verEstrato(conta, senha)
        if len(estratos) != 0:
            for i in estratos:
                print(traduzir.traduzir("Em {}, as {}, {}", estratos[i]["data"], estratos[i]["hora"], estratos[i]["mensagem"]))
            break
        print(traduzir.traduzir("Conta ou senha incorretas"))