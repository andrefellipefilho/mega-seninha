# Gera um APOSTAS.TXT grande com CPFs validos e apostas aleatorias
import random

ARQUIVO = "APOSTAS.txt"
QTD_APOSTAS = 100000
QTD_NUMEROS = 6
MAX_NUMERO = 60


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


def calcular_digito(digitos, peso_inicial):
    """Calcula um digito verificador do CPF."""
    soma = 0
    for i in range(len(digitos)):
        soma = soma + digitos[i] * (peso_inicial - i)
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    return resto


def gerar_cpf():
    """Gera um CPF valido, so com digitos (11 caracteres)."""
    digitos = []
    for i in range(9):
        digitos.append(random.randint(0, 9))
    digitos.append(calcular_digito(digitos, 10))
    digitos.append(calcular_digito(digitos, 11))
    texto = ""
    for d in digitos:
        texto = texto + str(d)
    return texto


def main():
    arquivo = open(ARQUIVO, "w")
    # Primeira linha: sorteio padrao (so usado se escolher 'n' no programa)
    arquivo.write(formatar_numeros(sortear_numeros()) + "\n")
    for i in range(QTD_APOSTAS):
        arquivo.write(gerar_cpf() + "\n")
        arquivo.write(formatar_numeros(sortear_numeros()) + "\n")
    arquivo.close()
    print("Arquivo", ARQUIVO, "gerado com", QTD_APOSTAS, "apostas.")


main()