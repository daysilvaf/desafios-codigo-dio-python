DESAFIO
Imagine que você está desenvolvendo um aplicativo para um banco que deseja calcular os juros compostos de um investimento. Seu 
objetivo é criar uma função que receba três parâmetros: o valor inicial do investimento, a taxa de juros anual e o período de 
tempo em anos. A função deve calcular e retornar o valor final do investimento após o período determinado, levando em consideração 
os juros compostos.

ENTRADA
A função deve receber os seguintes parâmetros:
valor_inicial: um número inteiro ou decimal representando o valor inicial do investimento.
taxa_juros: um número decimal representando a taxa de juros anual. Por exemplo, se a taxa for de 5%, o valor passado será 0.05.
periodo: um número inteiro representando a quantidade de anos do investimento.

SAÍDA
A função deve retornar o valor final do investimento após o período determinado, considerando os juros compostos. O valor final 
deve ser arredondado para duas casas decimais.

EXEMPLOS
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu 
programa com esses exemplos e com outros casos possíveis.

------------------------------------------------------
| ENTRADA |                   SAÍDA                  |
------------------------------------------------------
|   5000  |  Valor final do investimento: R$ 7346.64 |
|   0.08  |                                          |
|   5     |                                          |
------------------------------------------------------
|   1000  |  Valor final do investimento: R$ 1191.02 |
|   0.06  |                                          |
|   3     |                                          |
------------------------------------------------------
|   20000 | Valor final do investimento: R$ 29604.89 |
|   0.04  |                                          |
|   10    |                                          |
------------------------------------------------------

RESOLUÇÃO DO DESAFIO

def calcular_valor_final(valor_inicial, taxa_juros, periodo):
    valor_final = valor_inicial * (1 + taxa_juros) ** periodo
return round(valor_final, 2)

valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = calcular_valor_final(valor_inicial, taxa_juros, periodo)

print(f"Valor final do investimento: R$ {valor_final:.2f}")
