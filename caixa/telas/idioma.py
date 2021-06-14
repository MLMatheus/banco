from arquivo import arquivo
from gerente.telas import listararquivos
from caixa import funcoescaixa
from caixa import traduzir

def idioma():
    arquivos = arquivo.pegarArquivos("../lang")
    listararquivos.listar(arquivos, True)
    while True:
        numero = int(input(traduzir.traduzir("Qual o número correspondente ao idioma escolhido")))
        if numero >= len(arquivos) or numero < 0:
            print(traduzir.traduzir("Número inválido"))
            continue
        funcoescaixa.auterarIdioma(arquivos[numero])
        break