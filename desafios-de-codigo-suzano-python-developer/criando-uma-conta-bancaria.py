DESCRIÇÃO
Implemente uma classe chamada ContaBancaria para representar uma conta bancária simples. Essa classe deve permitir que você realize as operações básicas de uma conta: depósito, saque e consulta de saldo. O saldo negativo.

REQUISITOS
A classe ContaBancaria deve ter:
ATRIBUTOS
titular (nome do dono da conta).
saldo (saldo inicial, que começa com 0 por padrão).
MÉTODOS
depositar(valor): adiciona o valor informado ao saldo.
sacar(valor): subtrai o valor informado do saldo, se houver saldo suficiente. Caso contrário, exiba a mensagem "Saque não permitido".
saldo_atual(): retorna o saldo atual da conta.

ENTRADA
Entrada
1.  Nome do titular (string).
2.  Sequência de valores representando operações de depósito e saque:
Valores positivos representam depósitos.
Valores negativos representam saques.

SAÍDA
Exiba as operações realizadas e o saldo final no formato:  "Operações: +500, -200; Saldo: 300"

EXEMPLOS
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

-------------------------------------------------------------------------------------
|       ENTRADA       |                            SAÍDA                            | 
-------------------------------------------------------------------------------------
|        Maria        | Operações: +100, -50, +200, Saque não permitido; Saldo: 250 | 
| 100, -50, 200, -300 |                                                             |
-------------------------------------------------------------------------------------
|       Carlos        |   Operações: +1000, -500, Saque não permitido; Saldo: 500   | 
|  1000, -500, -600   |                                                             |
-------------------------------------------------------------------------------------
|         Ana         |                Operações: 0, +100; Saldo: 100               | 
|        0, 100       |                                                             |
-------------------------------------------------------------------------------------

RESOLUÇÃO 

class ContaBancaria:
  def __init__(self, titular):
    # TODO: Inicialize a conta bancária com o nome do titular, saldo 0 e  liste para armazenar as operações realizadas:
    self.titular = titular
    self.saldo = 0
    self.operacoes = []
    
  def depositar(self, valor):
    # TODO: Implemente o método para realizar um depósito, adicione o valor ao saldo e registre a operação:
    self.saldo += valor
    self.operacoes.append("+" + str(valor))
    
  def sacar(self, valor):
    # TODO: Implemente o método para realizar um saque:
    # TODO: Verifique se há saldo suficiente para o saque
    if self.saldo >= abs(valor):
      # TODO: Subtraia o valor do saldo (valor já é negativo)
      self.saldo += valor
      # TODO: Registre a operação e retorne a  mensagem de saque negado
      self.operacoes.append(str(valor))
    else:
      self.operacoes.append("Saque não permitido")
      
  def saldo_atual(self):
    return self.saldo
    
  def extrato(self):
    # TODO: Crie o método para exibir o extrato da conta e junte as operações no formato correto:
    print("Operações: " + ", ".join(self.operacoes) + "; Saldo: " + str(self.saldo))
    
nome_titular = input().strip()
conta = ContaBancaria(nome_titular)

entrada_transacoes = input().strip()
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

for valor in transacoes:
  if valor > 0:
    conta.depositar(valor)
  else:
    conta.sacar(valor)
    
conta.extrato()
