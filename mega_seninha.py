# Mega-Seninha - Paradigmas de Linguagens de Programacao
# Paradigma: puramente imperativo (apenas funcoes e procedimentos)
import random

ARQUIVO_ENTRADA = "APOSTAS.txt"
ARQUIVO_GANHADORES = "GANHADORES.TXT"
ARQUIVO_RESULTADO = "RESULTADO.TXT"
QTD_NUMEROS = 6
MAX_NUMERO = 60
MAX_QUADRAS_NA_TELA = 10


def ler_linhas(nome_arquivo):
    """Le o arquivo e devolve uma lista com as linhas nao vazias."""
    arquivo = open(nome_arquivo, "r")
    linhas = []
    for linha in arquivo:
        linha = linha.strip()
        if linha != "":
            linhas.append(linha)
    arquivo.close()
    return linhas


def converter_numeros(linha):
    """Converte '14 23 53 56 57 60' em uma lista de inteiros."""
    partes = linha.split(" ")
    numeros = []
    for parte in partes:
        numeros.append(int(parte))
    return numeros


def sortear_numeros():
    """Sorteia QTD_NUMEROS numeros distintos, em ordem crescente."""
    numeros = []
    while len(numeros) < QTD_NUMEROS:
        n = random.randint(1, MAX_NUMERO)
        if n not in numeros:
            numeros.append(n)
    numeros.sort()
    return numeros


def formatar_numeros(numeros):
    """Transforma [1, 14, 60] em '01 14 60'."""
    texto = ""
    for i in range(len(numeros)):
        if i > 0:
            texto = texto + " "
        texto = texto + "%02d" % numeros[i]
    return texto


def contar_acertos(sorteados, aposta):
    """Conta quantos numeros da aposta aparecem entre os sorteados."""
    acertos = 0
    for numero_aposta in aposta:
        for numero_sorteado in sorteados:
            if numero_aposta == numero_sorteado:
                acertos = acertos + 1
    return acertos


def formatar_cpf(cpf):
    """Transforma 12345678909 em 123.456.789-09."""
    return cpf[0:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:11]


def encontrar_premiados(linhas, sorteados):
    """Devolve tres listas de CPFs: [sena, quina, quadra]."""
    sena = []
    quina = []
    quadra = []

    i = 1
    while i + 1 < len(linhas):
        cpf = formatar_cpf(linhas[i])
        aposta = converter_numeros(linhas[i + 1])
        acertos = contar_acertos(sorteados, aposta)
        if acertos == 6:
            sena.append(cpf)
        elif acertos == 5:
            quina.append(cpf)
        elif acertos == 4:
            quadra.append(cpf)
        i = i + 2

    return [sena, quina, quadra]


def escrever_lista(arquivo, titulo, lista):
    """Escreve um titulo e um CPF por linha."""
    arquivo.write(titulo + " (" + str(len(lista)) + "):\n")
    for cpf in lista:
        arquivo.write("  " + cpf + "\n")


def escrever_ganhadores(nome_arquivo, sena):
    """GANHADORES.TXT: apenas os CPFs da sena, um por linha."""
    arquivo = open(nome_arquivo, "w")
    for cpf in sena:
        arquivo.write(cpf + "\n")
    arquivo.close()


def escrever_resultado(nome_arquivo, sorteados, sena, quina, quadra):
    """RESULTADO.TXT: sorteio e todos os premiados."""
    arquivo = open(nome_arquivo, "w")
    arquivo.write("Numeros sorteados: " + formatar_numeros(sorteados) + "\n\n")
    escrever_lista(arquivo, "SENA (6 acertos)", sena)
    escrever_lista(arquivo, "QUINA (5 acertos)", quina)
    escrever_lista(arquivo, "QUADRA (4 acertos)", quadra)
    arquivo.close()


def mostrar_lista(titulo, lista, limite):
    """Mostra na tela os CPFs de uma lista (ate 'limite')."""
    print(titulo + ":", len(lista))
    mostrados = 0
    for cpf in lista:
        if mostrados < limite:
            print("   ", cpf)
            mostrados = mostrados + 1
    if len(lista) > limite:
        print("    ... e mais", len(lista) - limite, "(veja RESULTADO.TXT)")


def mostrar_resultado(sorteados, sena, quina, quadra):
    print("")
    print("==============================")
    print(" NUMEROS SORTEADOS:", formatar_numeros(sorteados))
    print("==============================")
    mostrar_lista("SENA (6 acertos)", sena, len(sena))
    mostrar_lista("QUINA (5 acertos)", quina, len(quina))
    mostrar_lista("QUADRA (4 acertos)", quadra, MAX_QUADRAS_NA_TELA)
    print("")


def main():
    linhas = ler_linhas(ARQUIVO_ENTRADA)

    resposta = input("Sortear novos numeros agora? (s/n): ")
    if resposta == "s":
        sorteados = sortear_numeros()
    else:
        sorteados = converter_numeros(linhas[0])

    premiados = encontrar_premiados(linhas, sorteados)
    sena = premiados[0]
    quina = premiados[1]
    quadra = premiados[2]

    escrever_ganhadores(ARQUIVO_GANHADORES, sena)
    escrever_resultado(ARQUIVO_RESULTADO, sorteados, sena, quina, quadra)
    mostrar_resultado(sorteados, sena, quina, quadra)


main()