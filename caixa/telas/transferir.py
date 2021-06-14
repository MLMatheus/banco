from caixa import funcoescaixa
from caixa import traduzir

def transferir():
    while True:
        conta = input(traduzir.traduzir("Informe o número da sua conta: "))
        contaDestino = input(traduzir.traduzir("Informe o número da conta para qual quer transferir: "))
        valor = float(input(traduzir.traduzir("Informe o valor que deseja transferir: ")))
        senha = input(traduzir.traduzir("Informe sua senha numérica de 6 dígitos: "))
        resultado = funcoescaixa.transferir(conta, contaDestino, valor, senha)
        if resultado == 0:
            print(traduzir.traduzir("Conta de origem inválida"))
        elif resultado == 1:
            print(traduzir.traduzir("Conta de destino inválida"))
        elif resultado == 2:
            print(traduzir.traduzir("Saldo insuficiente"))
            break
        elif resultado == 3:
            print(traduzir.traduzir("Senha incorreta"))
        else:
            print(traduzir.traduzir("Transferência realisada com sucesso!"))
            break