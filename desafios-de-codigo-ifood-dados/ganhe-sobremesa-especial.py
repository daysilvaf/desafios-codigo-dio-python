DESAFIO
Crie um programa que informe ao usuário se ele pode receber um brinde especial de acordo com o valor total do pedido. Se o valor total do pedido for maior ou igual a 
R$ 50.00, o usuário receberá uma sobremesa grátis. Caso contrário, o usuário não receberá nenhum brinde.

ENTRADA
A entrada deverá receber o valor total do pedido em uma variável numérica:
valorPedido: o valor do pedido.

SAÍDA
Deverá retornar uma mensagem (string) que informa se o usuário ganhou uma sobremesa ou não:
Se valorPedido >= 50, a mensagem deve ser:
Parabens, você ganhou uma sobremesa gratis!
Caso contrário, a mensagem deve ser:
Que pena, você nao ganhou nenhum brinde especial.
Desafio Bônus: Utilize interpolação de strings para formatar sua saída ao invés da concatenação de strings tradicional.

EXEMPLOS
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos 
possíveis.

---------------------------------------------------------------
| ENTRADA |                        SAÍDA                      |
---------------------------------------------------------------
|    60   |    Parabens, você ganhou uma sobremesa gratis!    |
|    30   | Que pena, você nao ganhou nenhum brinde especial. |
|    90   |    Parabens, você ganhou uma sobremesa gratis!    |
---------------------------------------------------------------

RESOLUÇÃO DO DESAFIO

valorPedido = float(input())

# Verificação das condições para impressão da saída utilizando interpolação de strings
if valorPedido >= 50:
    mensagem_saida = "Parabens, você ganhou uma sobremesa gratis!"
else:
    mensagem_saida = "Que pena, você nao ganhou nenhum brinde especial."

print(mensagem_saida)
