DESAFIO
Crie um programa que leia 6 valores, os quais poderão ser negativos e/ou positivos. Em seguida, apresente a quantidade de valores positivos digitados.

ENTRADA
Você receberá seis valores, negativos e/ou positivos.

SAÍDA
Exiba uma mensagem dizendo quantos valores positivos foram lidos. assim como é exibido abaixo no exemplo de saída. Não se esqueça de incluir na 
mensagem de saída o sufixo "valores positivos", conforme o exemplo abaixo:

--------------------------------------------
| EXEMPLO DE ENTRADA |   EXEMPLO DE SAÍDA  | 
--------------------------------------------
|          7         | 4 valores positivos |
|         -5         |                     |
|          6         |                     |
|        -3.4        |                     |
|         4.6        |                     |
|         12         |                     |
--------------------------------------------

RESOLUÇÃO DO DESAFIO

counter = 0

for _ in range(6):
    number = float(input())
    if number > 0:
        counter += 1

print("{} valores positivos".format(counter))
