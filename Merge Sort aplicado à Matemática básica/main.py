import json
import os

# Função merge_sort: Ordena a lista de conceitos utilizando o algoritmo Merge Sort.
# O algoritmo divide recursivamente a lista de conceitos em duas metades até que as sublistas tenham um ou zero elementos.
# Depois, ele as mescla de forma ordenada utilizando a função merge.
def merge_sort(conceitos, chave="dificuldade"):
    if len(conceitos) <= 1:  # Caso base da recursão: se a lista tiver um ou zero elementos, está ordenada.
        return conceitos

    meio = len(conceitos) // 2  # Divide a lista ao meio.
    esquerda = merge_sort(conceitos[:meio], chave)  # Ordena a metade esquerda.
    direita = merge_sort(conceitos[meio:], chave)  # Ordena a metade direita.

    return merge(esquerda, direita, chave)  # Junta as metades ordenadas de volta em uma lista ordenada.

# Função merge: Recebe duas listas (esquerda e direita) e as mescla de forma ordenada.
# A ordenação é feita com base na chave fornecida (por padrão, "dificuldade").
def merge(esquerda, direita, chave):
    resultado = []
    i = j = 0  # Índices para percorrer as listas esquerda e direita.

    # Mescla as duas listas, mantendo a ordem de acordo com a chave (dificuldade).
    while i < len(esquerda) and j < len(direita):
        if esquerda[i][chave] <= direita[j][chave]:
            resultado.append(esquerda[i])  # Adiciona o elemento da lista esquerda.
            i += 1
        else:
            resultado.append(direita[j])  # Adiciona o elemento da lista direita.
            j += 1

    # Se ainda restarem elementos na lista esquerda ou direita, adiciona-os ao resultado.
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado  # Retorna a lista mesclada e ordenada.

# Função exibir_exemplo: Mostra o conteúdo de um arquivo Markdown (MD) correspondente ao conceito.
# O arquivo de exemplo está localizado na pasta 'exemplos/nivel_{nivel}' e é nomeado de acordo com o nome do conceito.
def exibir_exemplo(conceito):
    nivel = conceito['dificuldade']
    nome_arquivo = f"exemplos/nivel_{nivel}/{conceito['nome'].lower().replace(' ', '_')}.md"
    
    # Verifica se o arquivo de exemplo existe e o exibe.
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            print(arquivo.read())
    else:
        print(f"Exemplo para {conceito['nome']} ainda não disponível.")  # Caso o arquivo não exista.

# Função carregar_dados: Carrega os dados do arquivo JSON contendo os conceitos matemáticos.
# O arquivo JSON é lido e seu conteúdo é retornado como uma lista de dicionários.
def carregar_dados():
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)  # Retorna os dados do arquivo JSON como um dicionário.

# Função salvar_dados: Salva os dados ordenados no arquivo "dados_ordenados.json".
# Isso permite manter os dados organizados para futuras execuções ou manipulações.
def salvar_dados(dados):
    with open("dados_ordenados.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)  # Salva os dados no formato JSON, com indentação.

# Função escolher_conceito: Exibe os conceitos ordenados e permite ao usuário escolher um para ver o exemplo.
# O usuário pode escolher um número correspondente ao conceito ou digitar 'sair' para encerrar.
def escolher_conceito(conceitos_ordenados):
    print("\nEscolha um conceito para ver o exemplo ou digite 'sair' para sair:")
    for i, conceito in enumerate(conceitos_ordenados, start=1):
        print(f"{i}. {conceito['nome']} - Nível {conceito['dificuldade']} ({conceito['grupo']})")
    
    escolha = input("> ").strip()
    
    if escolha.lower() == 'sair':
        return None  # Retorna None para encerrar o loop
    elif escolha.isdigit():  # Se a escolha for um número, busca o conceito correspondente.
        indice = int(escolha) - 1
        if 0 <= indice < len(conceitos_ordenados):
            conceito_escolhido = conceitos_ordenados[indice]
            exibir_exemplo(conceito_escolhido)  # Exibe o exemplo do conceito escolhido.
            return True  # Retorna True para continuar escolhendo
        else:
            print("Opção inválida. Tente novamente.")  # Caso o número esteja fora do intervalo de opções.
            return True
    else:
        print("Entrada inválida. Tente novamente.")  # Caso o usuário digite algo que não seja válido.
        return True

# Função principal que executa o fluxo do programa.
if __name__ == "__main__":
    print("Carregando conceitos matemáticos...")
    conceitos = carregar_dados()  # Carrega os dados de conceitos matemáticos do arquivo JSON.

    print("\nOrdenando conceitos por dificuldade...")
    conceitos_ordenados = merge_sort(conceitos, chave="dificuldade")  # Ordena os conceitos utilizando o Merge Sort.

    print("\nConceitos ordenados:")
    for conceito in conceitos_ordenados:
        print(f"{conceito['nome']} - Nível {conceito['dificuldade']} ({conceito['grupo']})")  # Exibe os conceitos ordenados.

    # Loop para o usuário escolher um conceito ou sair.
    while escolher_conceito(conceitos_ordenados):
        pass  # Continua pedindo ao usuário para escolher conceitos até que ele digite 'sair'.

    print("\nSaindo do programa.")
    salvar_dados(conceitos_ordenados)  # Salva os dados ordenados no arquivo JSON após a execução.
