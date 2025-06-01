DESAFIO
Você foi contratado para auxiliar na construção de uma nova plataforma de blog. Uma das funcionalidades solicitadas é um limitador de texto para exibir resumos de postagens na página inicial do site. Para isso, é necessário criar um programa que receba 
um tamanho máximo de caracteres permitido e o conteúdo do texto original, e então gere uma versão resumida desse conteúdo.
No entanto, o código desenvolvido inicialmente pela equipe contém erros lógicos que impedem o funcionamento correto da limitação de texto. Seu desafio é analisar, identificar e corrigir o erro para que o programa funcione como esperado.
Uma opção para te ajudar durante o processo de depuração é o uso do GitHub Copilot, que pode explicar e sugerir correções de código.

ENTRADA
A primeira linha da entrada será um número inteiro N (3 ≤ N ≤ 60), representando o número máximo de caracteres permitidos no resumo (incluindo as reticências, caso o texto seja cortado).
A segunda linha será uma string com até 60 caracteres, representando o texto do post.

SAÍDA
O programa deverá retornar o texto original sem modificações, caso ele tenha N ou menos caracteres.
Caso o texto ultrapasse o limite N, o programa deve:
Exibir os (N - 3) primeiros caracteres do texto original,
E adicionar ... ao final, completando o total de N caracteres.

EXEMPLOS
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

--------------------------------------------------------------------------------
|                  ENTRADA                  |               SAÍDA              | 
--------------------------------------------------------------------------------
|                      26                   |    Bem-vindo ao nosso blog...    | 
| Bem-vindo ao nosso blog sobre tecnologia. |                                  |
--------------------------------------------------------------------------------
|                      32                   | Aprenda a programar em Python... | 
| Aprenda a programar em Python hoje mesmo! |                                  |
--------------------------------------------------------------------------------
|                      20                   |            Olá, Mundo!           | 
|               Olá, Mundo!                 |                                  |
--------------------------------------------------------------------------------

RESOLUÇÃO

max_length = int(input())
user_input = input()

def summarize_text(text, limit):
    if len(text) <= limit:
        return text
    else:
        return text[:limit - 3] + "..."

output = summarize_text(user_input, max_length)

print(output)
