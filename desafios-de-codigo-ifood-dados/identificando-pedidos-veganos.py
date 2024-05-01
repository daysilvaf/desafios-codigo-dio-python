DESAFIO
O objetivo deste programa é ajudar a equipe do Restaurante Veggieworld a identificar rapidamente os pedidos veganos e não veganos e informar as calorias de cada prato definido 
pelo cliente. O programa deve solicitar ao usuário o número de pedidos que serão feitos e, em seguida, pedir informações sobre cada pedido, incluindo se o prato é vegano ou não 
(usando as opções "s" para sim e "n" para não) e a quantidade de calorias. Ao final, o programa deve exibir uma lista de todos os pedidos com suas informações correspondentes.

ENTRADA
Um inteiro n, que representa o número de pedidos que o usuário deseja fazer.
Para cada pedido, o usuário deve inserir:
O nome do prato;
A quantidade de calorias do prato;
Se o prato é vegano ou não (usando as opções "s" para sim e "n" para não).

SAÍDA
O programa deve exibir uma lista de todos os pedidos com suas informações correspondentes, incluindo o nome do prato, se é vegano ou não, e a quantidade de calorias, no 
seguinte formato:

Pedido X: NOME_DO_PRATO (EH_VEGANO?) - YYY calorias, onde "X" é o número do pedido, "NOME_DO_PRATO" é o nome do prato, "EH_VEGADO?" indica se o prato é vegano (escrever 
"Vegano" ou "Nao-vegano"), e "YYY" é a quantidade de calorias do prato.

EXEMPLOS
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros 
casos possíveis.

-------------------------------------------------------
|         ENTRADA        |            SAÍDA           | 
-------------------------------------------------------
|            1           |     Pedido 1: Hamburguer   | 
| Hamburguer de lentilha | de lentilha (Vegano) - 300 |
|           300          |          calorias          |
|            s           |                            |
-------------------------------------------------------
|            2           |    Pedido 1: Pizza (Nao-   |
|          Pizza         |   vegano) - 450 calorias   |
|           450          |                            |
|            n           |    Pedido 2: Sushi (Nao-   |
|          Sushi         |   vegano) - 200 calorias   |
|           200          |                            |
|            n           |                            |
-------------------------------------------------------

RESOLUÇÃO DO DESAFIO

numPedidos = int(input())

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = input()

if ehVegano == "s":
    ehVeganoTexto = "Vegano"
else:
    ehVeganoTexto = "Nao-vegano"

print(f"Pedido {i}: {prato} ({ehVeganoTexto}) - {calorias} calorias")
