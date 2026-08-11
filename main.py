import csv
import os
def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = input("Digite o ano de publicação do livro: ")
    with open('livros.csv', mode='a', newline='') as arquivo:
        escritor_csv = csv.writer(arquivo)
        escritor_csv.writerow([titulo, autor, ano])

print("Livro cadastrado com sucesso!")
print("======Biblioteca======")
print("1- Cadastrar livro")
print("2- Listar livros")
print("3- Pesquisar livro")
print("4- Registrar empréstimo")
print("5- Registrar devolução")
print("6- Ordenar livros")
print("7- Sair")
opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    cadastrar_livro()