DESAFIO
Em um sistema de cadastro online, os nomes dos usuários precisam ser formatados corretamente antes de serem armazenados no banco de dados. Para isso, você deve criar um programa que:
Receba um nome completo como entrada (ex: "joão da silva"),
E retorne esse nome com todas as palavras iniciando com letra maiúscula, enquanto o restante das letras permanece em minúsculo.
No entanto, o código inicial contém um erro de lógica que deve ser corrigido para que a capitalização funcione como esperado.
Uma opção para te ajudar durante o processo de depuração é o uso do GitHub Copilot, que pode explicar e sugerir correções de código.

ENTRADA
Uma única string representando o nome completo do usuário.
O nome pode conter entre 1 e 5 palavras.
Todas as letras podem estar em caixa baixa, alta ou mista.

SAÍDA
O programa deve imprimir o nome com cada palavra começando com letra maiúscula, e o restante das letras minúsculas.

EXEMPLOS
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

-----------------------------
|   ENTRADA   |    SAÍDA    | 
-----------------------------
| joão silva  | João Silva  |
-----------------------------
| MARIA cOSTA | Maria Costa |
-----------------------------
| lUcAs pIRES	| Lucas Pires | 
-----------------------------

RESOLUÇÃO

full_name = input()

def format_name(name):
    return name.title()

formatted = format_name(full_name)
print(formatted)
