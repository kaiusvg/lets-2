# Simulador de Máquina de Turing em Python

Este projeto implementa um simulador de Máquina de Turing que lê uma especificação em JSON e um arquivo de entrada em TXT, simula a máquina e gera a fita final em um arquivo de saída. Além disso, indica na linha de comando se a entrada foi aceita (1) ou rejeitada (0).

## Estrutura do Projeto

simulador.py - Código principal do simulador
 maquina.json - Arquivo JSON com a especificação da máquina
entrada.txt - Arquivo de entrada com palavras a serem testadas
 saida.txt - Arquivo de saída gerado pelo simulador




Exemplo de transição:

json
{
    "from": 0,
    "to": 1,
    "read": "a",
    "write": "X",
    "dir": "R"
}

Arquivo de Entrada

O arquivo de entrada (entrada.txt) deve conter uma palavra por linha, sem espaços extras. Cada linha será processada individualmente pela máquina de Turing.

Exemplo:

aab
abc
cba


Exemplo:

python simulador.py maquina.json entrada.txt saida.txt


A fita final de cada entrada será escrita em saida.txt.

No terminal será exibido 1 se a entrada for aceita ou 0 se for rejeitada.

Exemplo de Saída

Para a entrada:

aab

A saída pode ser:

XXB

E na linha de comando será exibido:

1

conforme:

{
    "initial" : 0,
    "final" : [4],
    "white" : "_",
    "transitions" : [
        {"from": 0, "to": 1, "read": "a", "write": "A", "dir":"R"},
        {"from": 1, "to": 1, "read": "a", "write": "a", "dir":"R"},
        {"from": 1, "to": 1, "read": "B", "write": "B", "dir":"R"},
        {"from": 1, "to": 2, "read": "b", "write": "B", "dir":"L"},
        {"from": 2, "to": 2, "read": "B", "write": "B", "dir":"L"},
        {"from": 2, "to": 2, "read": "a", "write": "a", "dir":"L"},
        {"from": 2, "to": 0, "read": "A", "write": "A", "dir":"R"},
        {"from": 0, "to": 3, "read": "B", "write": "B", "dir":"R"},
        {"from": 3, "to": 3, "read": "B", "write": "B", "dir":"R"},
        {"from": 3, "to": 4, "read": "", "write": "", "dir":"L"}      
    ]
