DESCRIÇÃO
Bancos de dados possuem diferentes arquiteturas e finalidades. Relacionais ou NoSQL, cada tipo tem um propósito específico. Neste desafio, seu objetivo é identificar corretamente o tipo de banco de dados.

ENTRADA
Informe o nome do banco de dados:
MySQL
MongoDB
Cosmos DB
SQL Server

SAÍDA
Retorne a categoria correta do banco:
Relacional
NoSQL
NoSQL (Distribuído)
Relacional

EXEMPLOS 

-----------------------------------
|  ENTRADA  |         SAÍDA       |
-----------------------------------
|   MySQL   |      Relacional     |
----------------------------------- 
|  MongoDB  |        NoSQL        |
----------------------------------- 
| Cosmos DB | NoSQL (Distribuído) |
-----------------------------------

RESOLUÇÃO

# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def tipo_banco(nome):
  if nome == "MySQL":
    return "Relacional"
  elif nome == "MongoDB":
    return "NoSQL"
  elif nome == "Cosmos DB":
    return "NoSQL (Distribuído)"
  elif nome == "SQL Server":
    return "Relacional"

print(tipo_banco(entrada))
