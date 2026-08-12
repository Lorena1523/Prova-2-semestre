# 📚 Sistema de Biblioteca

Este projeto é um sistema simples de gerenciamento de livros desenvolvido em **Python**. O programa funciona através do terminal e utiliza um arquivo **CSV** para armazenar as informações dos livros cadastrados.

O projeto foi desenvolvido como atividade da disciplina do **2º semestre**.

## 🎯 Objetivo

O objetivo do projeto é desenvolver um sistema de biblioteca utilizando conceitos básicos de programação em Python, como:

* Funções;
* Estruturas condicionais;
* Estruturas de repetição;
* Listas e dicionários;
* Manipulação de arquivos;
* Leitura e escrita de arquivos CSV;
* Pesquisa e ordenação de dados;
* Menu interativo no terminal.

## ⚙️ Funcionalidades

O sistema possui um menu com as seguintes opções:

### 1. Cadastrar livro

Permite cadastrar um novo livro informando:

* Título;
* Autor;
* Ano de publicação;
* Código/ISBN.

Ao cadastrar um livro, seu status é definido automaticamente como **Disponível**.

### 2. Listar livros

Exibe todos os livros cadastrados no arquivo `livros.csv`, mostrando:

* Título;
* Autor;
* Ano;
* Código/ISBN;
* Status.

### 3. Pesquisar livro

Permite pesquisar um livro utilizando o **título ou o autor**.

A pesquisa não diferencia letras maiúsculas e minúsculas, facilitando a localização dos livros.

### 4. Registrar empréstimo

Permite realizar o empréstimo de um livro utilizando seu código.

Caso o livro esteja disponível, seu status é alterado para:

```text
Emprestado
```

Caso já esteja emprestado, o sistema informa que o livro não está disponível.

### 5. Registrar devolução

Permite registrar a devolução de um livro através do código.

Quando um livro emprestado é devolvido, seu status volta para:

```text
Disponível
```

### 6. Ordenar livros

Exibe os livros cadastrados em **ordem alfabética pelo título**.

### 7. Sair

Encerra a execução do programa.

## 🗂️ Estrutura do projeto

```text
Prova-2-semestre/
│
├── main.py
├── livros.csv
└── README.md
```

### `main.py`

É o arquivo principal do projeto. Nele estão implementadas todas as funções do sistema e o menu de interação com o usuário.

### `livros.csv`

É o arquivo utilizado para armazenar os dados dos livros.

Atualmente, o arquivo possui as seguintes informações:

```csv
Titulo,Autor,Ano,Codigo/ISBN,Status
Meu pequeno aranha,Lorena Trindade,2009,020809,Disponível
Cates,Graciliano Ramos,2013,134340,Disponível
```

### `README.md`

Documento que apresenta informações sobre o projeto, suas funcionalidades e instruções para execução.

## 🛠️ Tecnologias utilizadas

* **Python 3**
* **CSV**
* Biblioteca padrão `csv`
* Biblioteca padrão `os`

Não é necessário instalar bibliotecas externas para executar o projeto.

## ▶️ Como executar

### 1. Clonar o repositório

Utilize o comando:

```bash
git clone https://github.com/Lorena1523/Prova-2-semestre.git
```

### 2. Entrar na pasta do projeto

```bash
cd Prova-2-semestre
```

### 3. Executar o programa

O arquivo principal do projeto é o `main.py`.

Execute:

```bash
python main.py
```

Caso seu computador utilize `python3`:

```bash
python3 main.py
```

## 💻 Menu do sistema

Ao executar o programa, será apresentado o seguinte menu:

```text
====== Biblioteca ======
1 - Cadastrar livro
2 - Listar livros
3 - Pesquisar livro
4 - Registrar empréstimo
5 - Registrar devolução
6 - Ordenar livros
7 - Sair
```

O usuário deve digitar o número correspondente à opção desejada.

## 💾 Armazenamento dos dados

Os dados são armazenados no arquivo `livros.csv`.

Quando um novo livro é cadastrado, o programa verifica se o arquivo existe. Caso não exista, o arquivo é criado juntamente com seu cabeçalho.

As informações são organizadas nas seguintes colunas:

| Campo         | Descrição                                       |
| ------------- | ----------------------------------------------- |
| `Titulo`      | Nome do livro                                   |
| `Autor`       | Nome do autor                                   |
| `Ano`         | Ano de publicação                               |
| `Codigo/ISBN` | Código de identificação do livro                |
| `Status`      | Indica se o livro está disponível ou emprestado |

## 🔄 Funcionamento do empréstimo e devolução

O sistema utiliza dois status principais:

```text
Disponível
Emprestado
```

Quando um livro disponível é emprestado:

```text
Disponível → Emprestado
```

Quando um livro emprestado é devolvido:

```text
Emprestado → Disponível
```

As alterações são salvas novamente no arquivo `livros.csv`.

## 📌 Observações

* O programa deve ser executado pelo arquivo `main.py`.
* O arquivo `livros.csv` é utilizado para armazenar os livros.
* O código/ISBN é utilizado para identificar o livro durante empréstimos e devoluções.
* Os dados são armazenados localmente em um arquivo CSV.
* O sistema funciona através do terminal.

## 👩‍💻 Autora

**Lorena**

## 🔗 Repositório

O código-fonte do projeto está disponível no GitHub:

[Prova-2-semestre — GitHub](https://github.com/Lorena1523/Prova-2-semestre?utm_source=chatgpt.com)
