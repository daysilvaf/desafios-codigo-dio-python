DESCRIÇÃO
Classificar corretamente os dados é o primeiro passo para uma análise confiável. Neste desafio, você deverá identificar o tipo de dado com base no valor apresentado.

ENTRADA
Informe um valor como texto:
123
31/12/2024
True
R$ 5.000,00

SAÍDA
Retorne o tipo de dado correspondente:
Número
Data
Booleano
Moeda

EXEMPLOS 

--------------------------
|   ENTRADA   |   SAÍDA  |
-------------------------- 
|     123     |  Número  |
-------------------------- 
|     True    | Booleano |
-------------------------- 
| R$ 5.000,00 |   Moeda  |
--------------------------

RESOLUÇÃO

# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def classificar_dado(valor):
  if valor == "123":
    return "Número"
  elif valor == "31/12/2024":
    return "Data"
  elif valor == "True":
    return "Booleano"
  elif valor == "R$ 5.000,00":
    return "Moeda"

print(classificar_dado(entrada))
