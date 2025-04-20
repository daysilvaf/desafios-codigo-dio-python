DESCRIÇÃO
Implemente uma classe ConversorTemperatura que converte temperaturas de Celsius para Fahrenheit. A classe deve incluir um método chamado celsius_para_fahrenheit que realiza o cálculo de conversão. 
A fórmula para converter de Celsius para Fahrenheit é:
Fahrenheit=(Celsius×95)+32Fahrenheit=(Celsius×59​)+32
Você também deverá criar uma instância do conversor e utilizar essa instância para realizar a conversão.

DOCUMENTAÇÃO OFICIAL
https://docs.python.org/pt-br/3/tutorial/classes.html
https://docs.python.org/pt-br/3/library/stdtypes.html#methods

ENTRADA
O programa deverá receber como entrada uma temperatura em graus Celsius fornecida pelo usuário.

SAÍDA
O programa deverá exibir a temperatura convertida para Fahrenheit.

EXEMPLOS
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses 
exemplos e com outros casos possíveis.

-------------------
| ENTRADA | SAÍDA | 
-------------------
|    32   |  89.6 | 
-------------------
|    22   |  71.6 |
-------------------
|    17   |  62.6 | 
-------------------

RESOLUÇÃO

#TODO: Crie uma classe para converter temperaturas de Celsius para Fahrenheit e um método que realiza o cálculo de conversão:

class Conversor:
  def __init__(self, celsius):
    self.celsius = celsius
    
  def celsius_para_fahrenheit(self, celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


# Entrada do usuário
celsius = float(input())

# TODO: Crie uma instância do conversor:

conversor = Conversor(celsius)

fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(fahrenheit)
