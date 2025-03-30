DESCRIÇÃO
Imagine que você trabalha no setor de TI de um banco e precisa criar um programa que registre as transações de uma conta bancária. Cada transação pode ser um depósito ou um saque, e todas elas serão armazenadas em uma lista. Seu programa deve 
calcular o saldo final da conta com base nas transações realizadas. Depósitos serão representados como valores positivos e saques como valores negativos.

ENTRADA
Uma lista contendo valores inteiros ou decimais representando as transações realizadas (ex.: [100, -50, 200]).
Valores positivos representam depósitos.
Valores negativos representam saques.

SAÍDA
O saldo final da conta no formato: "Saldo: R$ X.XX"

EXEMPLOS
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

----------------------------------------
|      ENTRADA      |       SAÍDA      | 
----------------------------------------
|  [100, -50, 200]  | Saldo: R$ 250.00 |
----------------------------------------
| [500, -200, -100] | Saldo: R$ 200.00 |
----------------------------------------
|  [250 -150, -50]  |  Saldo: R$ 50.00 | 
----------------------------------------

def calcular_saldo(transacoes):
    saldo = 0
    
    # Itera sobre cada transação na lista e atualiza o saldo
    for transacao in transacoes:
        saldo += transacao
    
    # Retorna o saldo formatado em moeda brasileira com duas casas decimais
    return f"Saldo: R$ {saldo:.2f}"

# Lendo a entrada do usuário
entrada_usuario = input()

# Formatando a entrada para converter em lista de números
entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")
transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# Calculando o saldo com base nas transações informadas
resultado = calcular_saldo(transacoes)

# Exibindo o resultado
print(resultado)
