from caixa.telas import depositar
from caixa.telas import sacar
from caixa.telas import checarsaldo
from caixa.telas import transferir
from caixa.telas import verestrato
from caixa.telas import idioma
from caixa import traduzir

def menu():
    while True:
        menu = input(traduzir.traduzir("Tecle sua opção:\nd - Depositar\ns - Sacar\ncs - Checar seu saldo\nf - Fazer uma transferência\nce - Checar seu estrato\nl - Auterar idioma do programa\nq - Sair do sistema")).lower()
        if menu == "d":
            depositar.depositar()
        if menu == "s":
            sacar.sacar()
        if menu == "cs":
            checarsaldo.checarSaldo()
        if menu == "f":
            transferir.transferir()
        if menu == "ce":
            verestrato.verEstrato()
        if menu == "l":
            idioma.idioma()
        if menu == "q":
            print(traduzir.traduzir("Obrigado por usar nossos serviços!"))
            break