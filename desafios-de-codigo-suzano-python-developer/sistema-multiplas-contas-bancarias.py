DESCRIÇÃO
Implemente um sistema que gerencie várias contas bancárias. Cada conta será representada como uma instância da classe ContaBancaria criada no desafio anterior. O sistema deve permitir que você crie contas para diferentes titulares e liste 
todas as contas cadastradas ao final da execução.

REQUISITOS
O sistema deve permitir:
Criar contas:  Ao criar uma conta, forneça o nome do titular e o saldo inicial no formato "Titular, SaldoInicial".
Listar contas:  Ao digitar o comando especial "FIM", o sistema deverá listar todas as contas cadastradas no formato especificado.

ENTRADA
O sistema deve permitir:
Criação de contas no formato: "Titular, SaldoInicial".
Um comando especial "FIM" será usado para encerrar o processo de entrada e listar as contas.

SAÍDA
Liste todas as contas cadastradas no formato: "Titular: X, Saldo: R$ Y"

EXEMPLOS
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

------------------------------------------------------------------
|    ENTRADA   |                      SAÍDA                      | 
------------------------------------------------------------------
|   João, 500  |	          João: R$ 500, Maria: R$ 1000         | 
|  Maria, 1000 |                                                 |
|      FIM     |                                                 |
------------------------------------------------------------------
|   Ana, 150   |            Ana: R$ 150, Bruno: R$ 250           |
|  Bruno, 250  |                                                 |
|      FIM     |                                                 |
------------------------------------------------------------------
| Fernando, 50 | Fernando: R$ 50, Gustavo: R$ 75, Helena: R$ 125 | 
|  Gustavo, 75 |                                                 |
|  Helena, 125 |                                                 |
|      FIM     |                                                 |
------------------------------------------------------------------

RESOLUÇÃO

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

class SistemaBancario:
    def __init__(self):
        self.contas = []

    def criar_conta(self, titular, saldo):
        nova_conta = ContaBancaria(titular, saldo)
        self.contas.append(nova_conta)


    def listar_contas(self):
        dados_contas = []  # Lista para armazenar os dados de cada conta formatados
        for conta in self.contas:
            dados_contas.append(f"{conta.titular}: R$ {conta.saldo}")
        print(", ".join(dados_contas))  # Imprime todos os dados formatados em uma única linha

sistema = SistemaBancario()

while True:
    entrada = input().strip()
    if entrada.upper() == "FIM":  
        break
    titular, saldo = entrada.split(", ")
    sistema.criar_conta(titular, int(saldo))

sistema.listar_contas()
