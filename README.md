# Mega-Seninha

Atividade 1 da disciplina **Paradigmas de Linguagens de Programação** (FNR), prof. Lin Tse-Min.

Solução computacional que gerencia um sistema de apostas similar à Mega-Sena. O programa sorteia 6 números, confere todas as apostas e mostra os CPFs dos ganhadores.

## Equipe

- André Fellipe Gomes 
- Carlos Fernando 

## Paradigma

Programação **puramente imperativa**, em Python: apenas procedimentos e funções como métodos de decomposição, sem classes e sem recursos funcionais (`map`, `filter`, `lambda`, list comprehension).

## Arquivos

| Arquivo | Função |
|---|---|
| `gerar_apostas.py` | Gera o `APOSTAS.TXT` com 100 mil apostas aleatórias e CPFs válidos |
| `mega_seninha.py` | Sorteia os números, confere as apostas e mostra o resultado |
| `APOSTAS.TXT` | Arquivo de entrada (gerado pelo `gerar_apostas.py`) |
| `GANHADORES.TXT` | Saída: CPFs que acertaram os 6 números (um por linha, com pontuação) |
| `RESULTADO.TXT` | Saída: sorteio completo, com sena, quina e quadra |

## Como executar

Requisito: **Python 3** instalado.

1. Coloque todos os arquivos na mesma pasta.
2. Gere as apostas (só precisa fazer uma vez):
```
   python gerar_apostas.py
```
   No Windows, se `python` não funcionar, use `py` no lugar.
3. Execute o programa:
```
   python mega_seninha.py
```
4. Quando perguntar *"Sortear novos numeros agora? (s/n)"*:
   - `s`: sorteia 6 números novos (muda a cada execução);
   - `n`: usa os 6 números da primeira linha do `APOSTAS.TXT`, conforme o enunciado.

## Formato do APOSTAS.TXT

- 1ª linha: os 6 números sorteados, em ordem crescente, separados por um espaço.
- Depois, cada aposta ocupa 2 linhas:
  - CPF do apostador (11 dígitos, sem pontuação);
  - os 6 números escolhidos, no mesmo formato da primeira linha.

Exemplo:

```
14 23 53 56 57 60
12345678909
14 23 53 56 57 60
63873418339
14 21 25 40 51 56
```

## Exemplo de saída

```
==============================
 NUMEROS SORTEADOS: 07 19 33 41 52 58
==============================
SENA (6 acertos): 0
QUINA (5 acertos): 2
    123.456.789-09
    519.087.236-02
QUADRA (4 acertos): 130
    ...
```

## Observação

Na Mega-Sena real a chance de acertar a sena é de 1 em 50 milhões. Para ter ganhadores da sena com mais frequência, altere `MAX_NUMERO` de 60 para 20 nos dois arquivos `.py`.
