from caixa import funcoescaixa
from caixa import traduzir

def depositar():
    while True:
        conta = input(traduzir.traduzir("Informe o número da conta de destino:"))
        para = int(input(traduzir.traduzir("Digite 1 para depositar em sua conta, 2 para depositar em uma conta diferente:")))
        valor = float(input(traduzir.traduzir("Qual valor que deseja depositar?")))
        modo = 0
        if para == 1:
            modo = 1
            senha = input(traduzir.traduzir("Informe sua senha numérica de 6 dígitos:"))
        elif para == 2:
            modo = 2
            senha = ""
        else:
            print(traduzir.traduzir("Opção inválida"))
        if modo != 0:
            if funcoescaixa.depositar(conta, valor, senha, modo):
                print(traduzir.traduzir("Valor depositado com sucesso!"))
                break
        print(traduzir.traduzir("Conta ou senha incorretos"))