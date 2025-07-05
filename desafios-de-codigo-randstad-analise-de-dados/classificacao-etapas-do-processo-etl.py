DESCRIÇÃO
O processo de ETL (Extração, Transformação e Carga) é central na engenharia de dados. Neste desafio, você deverá identificar a etapa do ETL com base na ação descrita.

ENTRADA
Informe uma ação de ETL:
Importar CSV do Azure
Remover espaços em branco
Inserir dados em um banco SQL
Converter datas para o formato padrão ISO

SAÍDA
Retorne a etapa correspondente:
Extração
Transformação
Carga
Transformação

EXEMPLOS 

-------------------------------------------------
|            ENTRADA            |     SAÍDA     |
------------------------------------------------- 
|     Importar CSV do Azure     |    Extração   |
------------------------------------------------- 
|   Remover espaços em branco   | Transformação |
------------------------------------------------- 
| Inserir dados em um banco SQL |     Carga     |
------------------------------------------------- 

RESOLUÇÃO

# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()


# Função responsável por receber um conceito e retornar sua respectiva descrição.
def etapa_etl(acao):
  if acao == "Importar CSV do Azure":
    return "Extração"


  # COMPLETE AQUI: Preencha corretamente cada conceito, considerando as descrições abaixo:
  elif acao == "Remover espaços em branco dos campos":
    return "Transformação"


  elif acao == "Inserir dados em um banco SQL":
    return "Carga"


  elif acao == "Converter datas para o formato padrão ISO":
    return "Transformação"


print(etapa_etl(entrada))
