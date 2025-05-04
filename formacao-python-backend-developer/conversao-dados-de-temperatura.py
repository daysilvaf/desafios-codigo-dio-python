DESCRIÇÃO
ocê está desenvolvendo um sistema de monitoramento de temperaturas para uma estação meteorológica. O seu script deve processar os dados brutos de temperaturas e converter esses dados de Celsius para Fahrenheit.
Para converter uma temperatura de Celsius para Fahrenheit, utiliza-se a fórmula matemática:
TF = (TC × 9/5) + 32

ONDE:
TF representa a temperatura em graus Fahrenheit,
TC representa a temperatura em graus Celsius.

ENTRADA
A entrada deve receber uma string com valores numéricos separados por “,” (vírgula) representando as temperaturas em graus Celsius.

SAÍDA
Deverá retornar uma lista de valores numéricos representando as temperaturas convertidas para Fahrenheit.

EXEMPLOS
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

----------------------------------------------------
|     ENTRADA    |               SAÍDA             | 
----------------------------------------------------
|  0,10,20,30,40 | [32.0, 50.0, 68.0, 86.0, 104.0] | 
----------------------------------------------------
| -5,-15,5,15,25 |  [23.0, 5.0, 41.0, 59.0, 77.0]  | 
----------------------------------------------------
|  12,25,30,18,5 |  [53.6, 77.0, 86.0, 64.4, 41.0] |
----------------------------------------------------

RESOLUÇÃO

# Recebe a entrada do usuário como uma string e divide essa string nos caracteres ',' (vírgula)
temperaturas_celsius = input().split(',')

# Função que converte uma lista de temperaturas em Celsius para Fahrenheit
def converter_celsius_para_fahrenheit(temperaturas_celsius):
    # Converte cada item da lista para float
    temperaturas_celsius = [float(temp) for temp in temperaturas_celsius]
    
    # Calcula as temperaturas em Fahrenheit usando a fórmula
    temperaturas_fahrenheit = [(temp * 9/5) + 32 for temp in temperaturas_celsius]
    
    return temperaturas_fahrenheit

# Imprime o resultado das temperaturas convertidas para Fahrenheit
print(converter_celsius_para_fahrenheit(temperaturas_celsius))
