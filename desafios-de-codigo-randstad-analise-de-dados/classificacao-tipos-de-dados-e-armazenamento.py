DESCRIÇÃO
Na ciência de dados, diferentes formatos de dados exigem diferentes tipos de armazenamento. Entender qual tipo de dado deve ser armazenado em qual sistema é fundamental para garantir eficiência, escalabilidade 
e organização. Neste desafio, você irá associar o tipo de dado ao local de armazenamento mais apropriado.

ENTRADA
Informe o tipo de dado:
Imagem
Transações Bancárias
Logs de Servidor
Documentos Word

SAÍDA
Retorne o local ideal de armazenamento para o tipo de dado informado.
Blob Storage
Banco de Dados Relacional
Data Lake
SharePoint

EXEMPLOS
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

----------------------------------------------------
|        ENTRADA       |           SAÍDA           | 
----------------------------------------------------
|        Imagem        |        Blob Storage       |
---------------------------------------------------- 
| Transações Bancárias | Banco de Dados Relacional |
---------------------------------------------------- 
|   Logs de Servidor   |         Data Lake         |
----------------------------------------------------

RESOLUÇÃO

# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def armazenar_dado(tipo):
  if tipo == "Imagem":
    return "Blob Storage"
  elif tipo == "Transações Bancárias":
    return "Banco de Dados Relacional"
  elif tipo == "Logs de Servidor":
    return "Data Lake"
  elif tipo == "Documentos Word":
    return "SharePoint"

print(armazenar_dado(entrada))
