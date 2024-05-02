DESAFIO - ALFABETO

Dada a letra N do alfabeto, nos diga qual a sua posição.

ENTRADA

Um único caracter N, uma letra maiúscula ('A'-'Z') do alfabeto (que contém 26 letras).

SAÍDA

Um único inteiro, que representa a posição da letra no alfabeto.

--------------------------------------------
| Exemplo de Entrada | Exemplo de Saída    |
--------------------------------------------
| C                  | 3                   |
--------------------------------------------
| J                  | 10                  |
--------------------------------------------
| Z                  | 26                  |
--------------------------------------------
| A                  | 1                   |
--------------------------------------------

RESOLUÇÃO DO DESAFIO

# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO ord(): Retorna o valor  ASCII de cada letra ou símbolo do teclado;

letra = input

#TODO: DE acordo com a entrada, imprima a posição dessa letra no Alfabeto: 

letra = input()
num = 0
soma = 0

num = ord(letra)
for i in range(65,91):
    soma = soma + 1
if i == num:
    print(soma)
    break
