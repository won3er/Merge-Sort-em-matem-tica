Projeto de Organização de Conceitos Matemáticos

Este projeto tem como objetivo organizar e apresentar conceitos matemáticos de forma interativa, utilizando o algoritmo Merge Sort para ordenar os conceitos por dificuldade e permitir a visualização de exemplos práticos. O sistema permite que o usuário escolha um conceito matemático de acordo com seu nível de dificuldade e visualize exemplos específicos a partir de arquivos Markdown.

Funcionalidades

Ordenação de Conceitos: Os conceitos matemáticos são organizados de acordo com sua dificuldade (Nível 1, Nível 2, Nível 3) utilizando o algoritmo Merge Sort, que é recursivo e eficiente para listas grandes.
Visualização de Exemplos: O projeto permite que o usuário escolha um conceito para visualizar um exemplo prático. Os exemplos estão armazenados em arquivos Markdown, organizados por nível de dificuldade.
Interatividade: O sistema interage com o usuário através de um menu onde ele pode selecionar os conceitos para visualizar ou sair do programa.

Persistência de Dados: Após a execução, os conceitos ordenados são salvos em um arquivo JSON para garantir que os dados organizados possam ser reutilizados em execuções subsequentes.

Como Funciona

Carregamento de Conceitos: Os dados dos conceitos matemáticos são carregados a partir de um arquivo JSON (dados.json), que contém uma lista de conceitos com seus respectivos níveis de dificuldade e grupos de conhecimento.
Ordenação de Conceitos: Utilizando o algoritmo Merge Sort, os conceitos são ordenados com base na chave "dificuldade".
Exibição de Exemplos: O usuário pode escolher um conceito para visualizar um exemplo prático, que está armazenado em arquivos Markdown na pasta exemplos/nivel_{nivel}.

Salvar Dados: Ao final do processo, os conceitos ordenados são salvos em um arquivo JSON (dados_ordenados.json), garantindo a persistência dos dados.

Estrutura de Pastas

exemplos/: Contém os arquivos Markdown com exemplos práticos dos conceitos organizados por nível de dificuldade (nivel_1, nivel_2, nivel_3).
dados.json: Arquivo JSON contendo os dados dos conceitos matemáticos com suas características, como nome, grupo e nível de dificuldade.
dados_ordenados.json: Arquivo JSON onde os conceitos ordenados são salvos após o processo de execução.

Como Usar

Instalação:

Clone o repositório ou baixe o projeto.
Certifique-se de ter o Python 3.x instalado.
Executar o Programa:

Execute o arquivo Python principal (projeto.py).
O sistema irá carregar os conceitos, ordená-los e apresentar um menu interativo para o usuário escolher conceitos e visualizar exemplos.
Exemplo de Execução:

Após o carregamento dos conceitos, você será solicitado a escolher um conceito.
Digite o número correspondente ao conceito que deseja ver o exemplo.

Para sair, digite sair.

Tecnologias Utilizadas
Python 3.x: Linguagem de programação utilizada para o desenvolvimento do projeto.
Algoritmo Merge Sort: Algoritmo de ordenação recursivo utilizado para ordenar os conceitos por dificuldade.
JSON: Formato de dados utilizado para armazenar e persistir os conceitos matemáticos.


