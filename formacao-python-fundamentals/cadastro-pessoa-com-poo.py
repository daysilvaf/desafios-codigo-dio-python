DESCRIÇÃO 
Neste desafio, temos a classe Pessoa com seus atributos que armazenam o nome e a idade de uma pessoa. Implemente um método para retornar uma representação formatada dos dados da pessoa, 
crie uma instância da pessoa e, por fim, chame o método para retornar as informações formatadas e imprimir o resultado. O objetivo é utilizarmos formas para criar e manipular objetos com POO, 
usando atributos e métodos para encapsular dados e comportamentos.

DOCUMENTAÇÃO OFICIAL
https://docs.python.org/pt-br/3/tutorial/classes.html
https://docs.python.org/pt-br/3/library/stdtypes.html#methods

ENTRADA
- Nome da pessoa (string)
- Idade da pessoa (inteiro)

SAÍDA
Uma string formatada com o nome e a idade da pessoa, no seguinte formato: Nome: {nome}, Idade: {idade}

EXEMPLOS
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

--------------------------------------------------
|    ENTRADA    |             SAÍDA              | 
--------------------------------------------------
|   Mary Silva  |   Nome: Mary Silva, Idade: 32  |
|       32      |                                |
--------------------------------------------------
|  John Soares  |  Nome: John Soares, Idade: 20  |
|       20      |                                |
--------------------------------------------------
| Marcelly Reis | Nome: Marcelly Reis, Idade: 40 |
|       40      |                                |
--------------------------------------------------

RESOLUÇÃO

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

#TODO: Crie um método para retornar as informações formatas com Nome e Idade:   

    def imprimir(self, nome, idade):
      print (f'Nome: {nome}, Idade: {idade}')
    
# Entrada do usuário

nome = input()
idade = int(input())

# TODO: Crie uma instância da pessoa:

pessoa = Pessoa(nome, idade) 

#TODO: Chame o método para retornar as informações formatadas e imprima o resultado:

pessoa.imprimir(nome, idade)
