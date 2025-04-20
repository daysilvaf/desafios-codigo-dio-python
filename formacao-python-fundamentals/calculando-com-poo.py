DESCRIÇÃO 
O desafio consiste em implementar uma classe Calculadora que utilize os princípios da Programação Orientada a Objetos (POO). A classe deve conter um método para realizar a operação de soma entre dois números inteiros, encapsulando assim a lógica matemática da adição.

DOCUMENTAÇÃO OFICIAL
https://docs.python.org/pt-br/3/tutorial/classes.html

ENTRADA
A entrada será composta por dois números inteiros fornecidos pelo usuário.

SAÍDA
A saída esperada é o resultado da soma dos dois números inteiros fornecidos como entrada.

EXEMPLOS
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

-------------------
| ENTRADA | SAÍDA | 
-------------------
|    5    |   10  |
|    5    |       |
-------------------
|    8    |   16  |
|    8    |       |
-------------------
|    20   |   30  |
|    10   |       |
-------------------

RESOLUÇÃO

# TODO: Crie uma classe e método para realizar a soma:

class Calculadora:
  def __init__(self, num1, num2, resultado=0):
    self.num1 = num1
    self.num2 = num2
    self._resultado = resultado
    
  def soma(self, num1, num2):
    self._resultado = num1 + num2
    return self._resultado 
    
num1 = int(input())
num2 = int(input())

# Criando uma instância da calculadora

calc = Calculadora(num1, num2)

resultado = calc.soma(num1, num2)
print(resultado)
