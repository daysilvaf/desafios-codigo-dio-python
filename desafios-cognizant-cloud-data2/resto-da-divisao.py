DESAFIO
Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da divisão por 5 for igual a 2 ou igual a 3.

ENTRADA
O arquivo de entrada contém 2 valores positivos inteiros quaisquer, não necessariamente em ordem crescente.

SAÍDA
Imprima todos os valores entre X e Y cujo resto da divisão por 5 for igual a 2 ou igual a 3, sempre em ordem crescente. Caso não existam valores no intervalo 
que satisfaçam a condição, a saída deve ser a palavra “error”.

EXEMPLOS
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos 
e com outros casos possíveis.

RESOLUÇÃO DO DESAFIO

X = int(input())
Y = int(input())

if Y > X:
    for i in range(X + 1, Y):
        if i % 5 == 2 or i % 5 == 3:
            print(i)

elif X > Y:
    for i in range(Y + 1, X):
        if i % 5 == 2 or i % 5 == 3:
            print(i)

else:
    print("error")
