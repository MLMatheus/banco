from gerente import funcoesgerente
from gerente.telas import imprimir
from gerente import traduzir

def cadastrar():
    while True:
        nome = input(traduzir.traduzir("Informe seu nome: "))
        cpf = input(traduzir.traduzir("Informe seu CPF: "))
        email = input(traduzir.traduzir("Informe seu E-mail: "))
        telefone = input(traduzir.traduzir("Informe seu telefone: "))
        endereco = input(traduzir.traduzir("Informe seu endereço completo: "))
        while True:
            tipoDeConta = input(traduzir.traduzir("Qual o tipo de conta? Digite p para poupança ou c para corrente"))
            if tipoDeConta.lower() == "p":
                break
            elif tipoDeConta.lower() == "c":
                break
            else:
                print(traduzir.traduzir("Opção inválida"))
        dados = funcoesgerente.cadastrarCliente(nome, cpf, email, telefone, endereco, tipoDeConta.lower())
        if dados == 0:
            print(traduzir.traduzir("O nome é obrigatório"))
        elif dados == 1:
            print(traduzir.traduzir("O CPF é obrigatório, ou está inválido"))
        elif dados == 2:
            print(traduzir.traduzir("O E-mail é obrigatório, ou já existe no sistema"))
        elif dados == 3:
            print(traduzir.traduzir("Telefone inválido ou em branco"))
        elif dados == 4:
            print(traduzir.traduzir("O endereço é obrigatório"))
        else:
            print(traduzir.traduzir("Cliente cadastrado com sucesso!"))
            print(traduzir.traduzir(dados))
            break
        print(traduzir.traduzir("Erro ao cadastrar cliente"))