DESAFIO
Você terá o desafio de ler um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma loja, e informe-o expresso no 
formato horas:minutos:segundos.

ENTRADA
O arquivo de entrada contém um valor inteiro N.

SAÍDA
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

-----------------------------------------
| EXEMPLO DE ENTRADA | EXEMPLO DE SAÍDA | 
-----------------------------------------
|         556        |      0:9:16      |
-----------------------------------------
|         1          | 	     0:0:1      |
-----------------------------------------

RESOLUÇÃO DO DESAFIO

segundos = int(input())

# Calcula as horas, minutos e segundos
horas = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
segundos = segundos % 60

# Imprime o resultado no formato horas:minutos:segundos
print("{}:{}:{}".format(horas, minutos, segundos))
