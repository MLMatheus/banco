from gerente import funcoesgerente
from gerente.telas import imprimir
from gerente import traduzir

def cadastrar():
    while True:
        nome = input(traduzir.traduzir("Informe o nome do gerente"))
        cpf = input(traduzir.traduzir("Informe os 11 dígitos do CPF"))
        email = input(traduzir.traduzir("Informe o email do gerente"))
        telefone = input(traduzir.traduzir("Informe o telefone do gerente"))
        while True:
            senha = input(traduzir.traduzir("Informe a senha de acesso: "))
            senha2 = input(traduzir.traduzir("Repita a senha digitada anteriormente: "))
            if senha == senha2:
                break
            print(traduzir.traduzir("As senhas digitadas não são iguais"))
        dados = funcoesgerente.cadastrarGerente(nome, cpf, email, telefone, senha)
        if dados == 0:
            print(traduzir.traduzir("O nome é obrigatório"))
        elif dados == 1:
            print(traduzir.traduzir("O CPF é obrigatório, ou está inválido"))
        elif dados == 2:
            print(traduzir.traduzir("O E-mail é obrigatório, ou já existe no sistema"))
        elif dados == 3:
            print(traduzir.traduzir("Telefone inválido ou em branco"))
        elif dados == 4:
            print(traduzir.traduzir("Senha em branco ou inválida"))
        else:
            print(traduzir.traduzir("Gerente cadastrado com sucesso!"))
            break
        print(traduzir.traduzir("Erro ao cadastrar gerente"))