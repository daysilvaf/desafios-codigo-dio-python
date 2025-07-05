DESCRIÇÃO
Comandos SQL são usados para interagir com bancos de dados. Neste desafio, identifique qual comando SQL está relacionado à ação descrita.

ENTRADA
Informe uma ação de banco de dados:
Inserir novo cliente
Atualizar e-mail do cliente
Excluir cliente
Listar todos os clientes

SAÍDA
Retorne o comando SQL correspondente:
INSERT
UPDATE
DELETE
SELECT

EXEMPLOS 

----------------------------------------
|           ENTRADA           |  SAÍDA |
---------------------------------------- 
|     Inserir novo cliente    | INSERT |
---------------------------------------- 
| Atualizar e-mail do cliente | UPDATE |
---------------------------------------- 
|   Listar todos os clientes  | SELECT |
---------------------------------------- 

RESOLUÇÃO

# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def comando_sql(acao):
  if acao == "Inserir novo cliente":
    return "INSERT"

  # COMPLETE AQUI: Preencha corretamente cada conceito, considerando as descrições abaixo:
  elif acao == "Atualizar e-mail do cliente":
    return "UPDATE"
  elif acao == "Excluir cliente":
    return "DELETE"
  elif acao == "Listar todos os clientes":
    return "SELECT"

print(comando_sql(entrada))
