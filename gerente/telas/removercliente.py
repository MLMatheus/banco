from gerente import funcoesgerente
from arquivo import arquivo
from gerente.telas import listar
from gerente.telas import confirmacao
from gerente.telas import imprimir
from gerente import traduzir

def remover():
    clientes = arquivo.ler("../gerente/clientes.json")
    while True:
        listar.listar(clientes, "nome", True)
        email = input(traduzir.traduzir("Informe o email do cliente a remover"))
        if arquivo.chaveExiste(clientes, "email", email):
            codigo = arquivo.codigoChave(clientes, "email", email)
            senha = input(traduzir.traduzir("Informe a senha da conta a ser removida:"))
            if clientes[codigo]["conta"]["saldo"] != 0:
                print(traduzir.traduzir("Ainda temos saldo em conta, não foi possível remover"))
                break
            if senha == clientes[codigo]["conta"]["senha"]:
                if confirmacao.confirmacao(traduzir.traduzir("Deseja remover a conta com o E-mail {}?", email)):
                    if funcoesgerente.removerCliente(codigo):
                        print(traduzir.traduzir("Removido com sucesso!"))
                        break
                    else:
                        print(traduzir.traduzir("Não foi possível remover, pois há uma ou mais transações pendentes para essa conta"))
                        break
                else:
                    print(traduzir.traduzir("Cancelado"))
                    break
            else:
                print(traduzir.traduzir("Senha incorreta"))
        else:
            print(traduzir.traduzir("Esse E-mail não existe"))