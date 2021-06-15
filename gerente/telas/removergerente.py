from gerente import funcoesgerente
from arquivo import arquivo
from gerente.telas import listar
from gerente.telas import confirmacao
from gerente.telas import imprimir
from gerente import traduzir

def remover():
    gerentes = arquivo.ler("../gerente/gerentes.json")
    while True:
        listar.listar(gerentes, "nome", True)
        email = input(traduzir.traduzir("Informe o E-mail do gerente a remover"))
        if arquivo.chaveExiste(gerentes, "email", email):
            codigo = arquivo.codigoChave(gerentes, "email", email)
            senha = input(traduzir.traduzir("Informe a senha da conta a ser removida:"))
            if senha == gerentes[codigo]["senha"]:
                if confirmacao.confirmacao(traduzir.traduzir("Deseja remover a conta com o E-mail {}?", email)):
                    funcoesgerente.removerGerente(codigo)
                    print(traduzir.traduzir("Removido com sucesso!"))
                    break
                else:
                    print(traduzir.traduzir("Cancelado"))
                    break
            else:
                print(traduzir.traduzir("Senha incorreta"))
        else:
            print(traduzir.traduzir("Esse E-mail não existe"))