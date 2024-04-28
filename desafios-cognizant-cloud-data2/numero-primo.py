Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido 
apenas pelo número 1 e pelo número 7.

ENTRADA
A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100), indicando o número de casos de teste da entrada. 
Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.

SAÍDA
Para cada caso de teste de entrada, imprima a mensagem “X eh primo” ou “X nao eh primo”, de acordo com a especificação fornecida.

-----------------------------------------
| EXEMPLO DE ENTRADA | EXEMPLO DE SAÍDA | 
-----------------------------------------
|          3         |  8 nao eh primo  |
|          8         |  51 nao eh primo |
|         51         |    7 eh primo    |
|          7         |                  |
-----------------------------------------

RESOLUÇÃO DO DESAFIO

n = int(input())
for i in range(n):
    num = int(input())
    divisors = 0

for j in range(1, (num+1)):
    if num % j == 0:
        divisors += 1

if divisors != 2:
    print(num, "nao eh primo")
else:
    print(num, "eh primo")
