DESCRIÇÃO 
Relacionamentos entre entidades em bancos de dados relacionais ajudam a organizar as informações e suas conexões. Neste desafio, você deverá identificar o tipo de relacionamento a partir de um cenário descrito.

ENTRADA 
Informe um cenário:
Cada funcionário tem um crachá exclusivo
Um cliente pode fazer muitos pedidos
Alunos podem cursar várias disciplinas e cada disciplina pode ter vários alunos
Um produto pertence a uma única categoria, mas uma categoria pode ter vários produtos

SAÍDA
Retorne o tipo de relacionamento:
1-1
1-N
N-N
1-N

EXEMPLOS 

-------------------------------------------------------------------------------------------
|                                     ENTRADA                                     | SAÍDA |
------------------------------------------------------------------------------------------- 
|                     Cada funcionário tem um crachá exclusivo                    |  1-1  |
------------------------------------------------------------------------------------------- 
|                      Um cliente pode fazer muitos pedidos                       |  1-N  |
------------------------------------------------------------------------------------------- 
| Alunos podem cursar várias disciplinas e cada disciplina pode ter vários alunos |  N-N  |
------------------------------------------------------------------------------------------- 

RESOLUÇÃO 

# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def tipo_relacionamento(cenario):
  if cenario == "Cada funcionário tem um crachá exclusivo":
    return "1-1"

# COMPLETE AQUI: Preencha corretamente cada conceito, considerando as 
  elif cenario == "Um cliente pode fazer muitos pedidos":
    return "1-N"
  elif cenario == "Alunos podem cursar várias disciplinas e cada disciplina pode ter vários alunos":
    return "N-N"
  elif cenario == "Um produto pertence a uma única categoria, mas uma categoria pode ter vários produtos":
    return "1-N"

print(tipo_relacionamento(entrada))
