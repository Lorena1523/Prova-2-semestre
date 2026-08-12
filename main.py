import csv
import os


# Cadastrando livros em um arquivo CSV
def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = input("Digite o ano de publicação do livro: ")
    codigo = input("Digite o código do livro: ")
    status = "Disponível"

    arquivo_existe = os.path.exists('livros.csv')

    with open('livros.csv', mode='a', newline='', encoding='utf-8') as arquivo:
        escritor_csv = csv.writer(arquivo)

        # Cria o cabeçalho somente se o arquivo ainda não existir
        if not arquivo_existe:
            escritor_csv.writerow(["Titulo", "Autor", "Ano", "Codigo/ISBN", "Status"])

        escritor_csv.writerow([titulo, autor, ano, codigo, status])

    print("Livro cadastrado com sucesso!")
    return True

#Esta funçao lista os livros cadastrados no arquivo CSV, exibindo suas informações de forma organizada.
# Esta função lista os livros cadastrados no arquivo CSV

def listar_livros():
    if not os.path.exists('livros.csv'):
        print("Nenhum livro cadastrado.")
        return

    with open('livros.csv', mode='r', newline='', encoding='utf-8') as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        livros = list(leitor_csv)

        if not livros:
            print("Nenhum livro cadastrado.")
            return

        print("\n--- LISTA DE LIVROS ---")
        for i, linha in enumerate(livros, start=1):
            # Limpa os espaços invisíveis ou quebras de linha das chaves do dicionário
            linha_limpa = {k.strip(): v for k, v in linha.items() if k is not None}
            
            print(
                f"{i}. Título: {linha_limpa.get('Titulo', 'N/A')} | "
                f"Autor: {linha_limpa.get('Autor', 'N/A')} | "
                f"Ano: {linha_limpa.get('Ano', 'N/A')} | "
                f"Código: {linha_limpa.get('Codigo/ISBN', 'N/A')} | "
                f"Status: {linha_limpa.get('Status', 'N/A')}"
            )
        print("-" * 25)

def pesquisar_livro():
    if not os.path.exists('livros.csv'):
        print("Nenhum livro cadastrado.")
        return

    termo_pesquisa = input("Digite o título ou autor do livro que deseja pesquisar: ").lower()

    with open('livros.csv', mode='r', newline='', encoding='utf-8') as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        livros_encontrados = []

# A função pesquisa livros no arquivo CSV com base no título ou autor fornecido pelo usuário.
# Ela percorre cada linha do arquivo, verificando se o termo de pesquisa está presente no título ou autor do livro. Se encontrar correspondências, adiciona os livros encontrados a uma lista e exibe os resultados de forma organizada. Caso nenhum livro seja encontrado, informa ao usuário que não há resultados correspondentes.
       
        for linha in leitor_csv:
            titulo = linha.get('Titulo', '').lower()
            autor = linha.get('Autor', '').lower()

            if termo_pesquisa in titulo or termo_pesquisa in autor:
                livros_encontrados.append(linha)

        if livros_encontrados:
            print("\n--- RESULTADOS DA PESQUISA ---")
            for i, livro in enumerate(livros_encontrados, start=1):
                print(
                    f"{i}. Título: {livro.get('Titulo')} | "
                    f"Autor: {livro.get('Autor')} | "
                    f"Ano: {livro.get('Ano')} | "
                    f"Código: {livro.get('Codigo/ISBN')} | "
                    f"Status: {livro.get('Status')}"
                )
            print("-" * 25)
        else:
            print("Nenhum livro encontrado com o termo pesquisado.")

# A função registrar_emprestimo() permite que o usuário registre o empréstimo de um livro. 
# Ela verifica se o arquivo 'livros.csv' existe e, em seguida, lista os livros disponíveis. O usuário é solicitado a digitar o código do livro que deseja emprestar. A função percorre os livros cadastrados, verificando se o código corresponde a algum livro. Se o livro estiver disponível, seu status é alterado para "Emprestado" e uma mensagem de sucesso é exibida. Caso contrário, uma mensagem informando que o livro não está disponível é mostrada. Se o código não for encontrado, uma mensagem de erro é exibida. Por fim, as alterações são salvas no arquivo CSV.

def registrar_emprestimo():
    if not os.path.exists('livros.csv'):
        print("Nenhum livro cadastrado.")
        return

    listar_livros()
    codigo = input("Digite o código do livro que deseja emprestar: ")

    with open('livros.csv', mode='r', newline='', encoding='utf-8') as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        livros = list(leitor_csv)

    livro_encontrado = False
    for livro in livros:
        if livro.get('Codigo/ISBN') == codigo:
            livro_encontrado = True
            if livro.get('Status') == 'Disponível':
                livro['Status'] = 'Emprestado'
                print(f"Livro '{livro.get('Titulo')}' emprestado com sucesso!")
            else:
                print(f"Livro '{livro.get('Titulo')}' não está disponível para empréstimo.")
            break

    if not livro_encontrado:
        print("Código de livro não encontrado.")

    with open('livros.csv', mode='w', newline='', encoding='utf-8') as arquivo:
        escritor_csv = csv.DictWriter(arquivo, fieldnames=['Titulo', 'Autor', 'Ano', 'Codigo/ISBN', 'Status'])
        escritor_csv.writeheader()
        escritor_csv.writerows(livros)   

# A função registrar_devolucao() permite que o usuário registre a devolução de um livro.
# Ela verifica se o arquivo 'livros.csv' existe e, em seguida, lista os livros cadastrados.
# O usuário é solicitado a digitar o código do livro que deseja devolver. A função percorre os livros cadastrados, verificando se o código corresponde a algum livro. Se o livro estiver emprestado, seu status é alterado para "Disponível" e uma mensagem de sucesso é exibida. Caso contrário, uma mensagem informando que o livro não está emprestado é mostrada. Se o código não for encontrado, uma mensagem de erro é exibida. Por fim, as alterações são salvas no arquivo CSV.

def registrar_devolucao():
    if not os.path.exists('livros.csv'):
        print("Nenhum livro cadastrado.")
        return

    listar_livros()
    codigo = input("Digite o código do livro que deseja devolver: ")

    with open('livros.csv', mode='r', newline='', encoding='utf-8') as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        livros = list(leitor_csv)

    livro_encontrado = False
    for livro in livros:
        if livro.get('Codigo/ISBN') == codigo:
            livro_encontrado = True
            if livro.get('Status') == 'Emprestado':
                livro['Status'] = 'Disponível'
                print(f"Livro '{livro.get('Titulo')}' devolvido com sucesso!")
            else:
                print(f"Livro '{livro.get('Titulo')}' não está emprestado.")
            break

    if not livro_encontrado:
        print("Código de livro não encontrado.")

    with open('livros.csv', mode='w', newline='', encoding='utf-8') as arquivo:
        escritor_csv = csv.DictWriter(arquivo, fieldnames=['Titulo', 'Autor', 'Ano', 'Codigo/ISBN', 'Status'])
        escritor_csv.writeheader()
        escritor_csv.writerows(livros)       

# A função ordenar_livros() ordena os livros cadastrados no arquivo CSV por título em ordem alfabética.

def ordenar_livros():
    if not os.path.exists('livros.csv'):
        print("Nenhum livro cadastrado.")
        return

    with open('livros.csv', mode='r', newline='', encoding='utf-8') as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        livros = list(leitor_csv)

    if not livros:
        print("Nenhum livro cadastrado.")
        return

    livros_ordenados = sorted(livros, key=lambda x: x.get('Titulo', '').lower())

    print("\n--- LIVROS ORDENADOS POR TÍTULO ---")
    for i, livro in enumerate(livros_ordenados, start=1):
        print(
            f"{i}. Título: {livro.get('Titulo', 'N/A')} | "
            f"Autor: {livro.get('Autor', 'Autor')} | "
            f"Ano: {livro.get('Ano', 'Ano')} | "
            f"Código: {livro.get('Codigo/ISBN', 'Código')} | "
            f"Status: {livro.get('Status', 'Status')}"
        )
    print("-" * 25)                  

while True:

    print("\n====== Biblioteca ======")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Registrar empréstimo")
    print("5 - Registrar devolução")
    print("6 - Ordenar livros")
    print("7 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
            cadastrar_livro()
        
    elif opcao == 2:
            listar_livros()

    elif opcao == 3:
            pesquisar_livro()

    elif opcao == 4:
            registrar_emprestimo()

    elif opcao == 5:
            registrar_devolucao()

    elif opcao == 6:
            ordenar_livros()

    elif opcao == 7:
            print("Programa encerrado.")
            break

    else:
            print("Opção não encontrada.")

