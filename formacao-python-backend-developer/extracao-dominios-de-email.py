DESCRIÇÃO
Os domínios de email são essenciais para categorizar e identificar a origem dos contatos, facilitando a segmentação e análise dos dados. Sabendo disso, sua função será receber uma string contendo múltiplos emails separados por ponto e vírgula e 
retornar uma lista contendo apenas os domínios de cada um desses emails.

ENTRADA
A entrada deve receber uma string contendo emails separados por ponto e vírgula: "email;email;email;...". Cada email é uma string.

SAÍDA 
Deverá retornar uma lista de strings com os domínios dos emails.

EXEMPLOS
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

------------------------------------------------------------------
|              ENTRADA             |             SAÍDA           | 
------------------------------------------------------------------
|    ana@example.com;bob@test.com  | ['example.com', 'test.com'] |
------------------------------------------------------------------
| carlos@empresa.com;maria@web.com |  ['empresa.com', 'web.com'] |
------------------------------------------------------------------
|          pedro@mail.com          |         ['mail.com']        | 
------------------------------------------------------------------

RESOLUÇÃO

# Recebe a entrada e armazena na variável "entrada"
entrada = input()

# Função responsável por extrair os domínios dos emails
def extrair_dominios(emails):
    # Separa os emails por ponto e vírgula
    lista_emails = emails.split(';')
    
    # Extrai o domínio de cada email usando split no '@'
    dominios = [email.split('@')[1] for email in lista_emails]
    
    return dominios

# Imprime a lista de strings com os domínios
print(extrair_dominios(entrada))
