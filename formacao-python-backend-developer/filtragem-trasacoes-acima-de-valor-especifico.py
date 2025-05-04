DESCRIÇÃO
Você está consumindo dados de uma API de uma instituição financeira que fornece uma lista de transações. Seu desafio é filtrar todas as transações que possuem um valor acima de um determinado limite.

ENTRADA
A entrada deve receber dois valores:
1. Um número decimal representando o valor limite.
2. Uma string contendo transações no seguinte formato: "ID:VALOR;ID:VALOR;..."

SAÍDA
Deverá retornar uma lista de strings, onde cada string contém as informações das transações cujo valor é maior que o valor limite especificado.

EXEMPLOS
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

--------------------------------------------------------
|           ENTRADA          |          SAÍDA          | 
|           150.00           | ['2:200.5', '3:150.75'] | 
| 1:100.00;2:200.50;3:150.75 |                         |
--------------------------------------------------------
|            300.00          |  ['4:500.0', '5:600.0'] |
|      4:500.00;5:600.00     |                         |
--------------------------------------------------------
|           100.00           | ['6:250.25', '8:110.5'] | 
|  6:250.25;7:90.00;8:110.50 |                         |
--------------------------------------------------------

RESOLUÇÃO

# Recebe o valor limite como entrada do usuário e converte para float
limite = float(input())

# Recebe a string de transações como entrada do usuário
transacoes = input()

# Define a função para filtrar transações acima do limite especificado
def filtrar_transacoes_acima_do_limite(limite, transacoes):
    if not transacoes:
        return []

    transacoes_filtradas = []
    lista_transacoes = transacoes.split(';')
    
    # Itera sobre cada transação na lista de transações
    for transacao in lista_transacoes:
        id_transacao, valor_str = transacao.split(':')
        valor = float(valor_str)
        
        # Verifica se o valor é maior que o limite
        if valor > limite:
            transacoes_filtradas.append(f"{id_transacao}:{valor}")

    return transacoes_filtradas
    
# Imprime as transações com valores acima do limite
print(filtrar_transacoes_acima_do_limite(limite, transacoes))
