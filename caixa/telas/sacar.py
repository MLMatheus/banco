from caixa import funcoescaixa
from caixa import traduzir

def sacar():
    while True:
        conta = input(traduzir.traduzir("Informe o número da sua conta:"))
        valor = float(input(traduzir.traduzir("Informe o valor que deseja sacar: ")))
        senha = input(traduzir.traduzir("Informe sua senha numérica de 6 dígitos: "))
        if funcoescaixa.sacar(conta, valor, senha):
            print(traduzir.traduzir("Valor sacado com sucesso!"))
            break
        print(traduzir.traduzir("Conta ou senha incorretas"))