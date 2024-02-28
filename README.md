# Sistema de Biblioteca

O projeto tem como intuito a fixação de conteúdos como Programação Orientada a Objetos e o Frameword python DJANGO, junto com a implementação de API (OPENAI)


## Funcionalidades

- CRUD de Livros
- Sistema de Login
- Cadastro de Usuários
- Cadastro e Listagem de Empréstimos
- Sinopse automática quando não cadastrada (API OPENAI)


## Aprendizados

Os principais conceitos adquitrido nesse projeto, foram os conceito e práticas de POO, o consumo de API, modelagem do desing do frontend usando o django templates, conceitos gerais do django (models, views, urls, forms, dentre outros conceitos)


## Stack utilizada

**Front-end:** Html (usando Django Templates), Css, JavaScript.

**Back-end:** Django (python)

**BD:** SQLite


## Documentação do DJANGO

[Documentação](https://docs.djangoproject.com/pt-br/5.0/)


## Documentação de Inicialização do Projeto

#### Instalação do VENV (Ambiente Virtual)

```bash
  python -m venv venv
```

#### Acessando o Ambiente Virtual (Windows)

```bash
  .\venv\Scripts\activate
```

#### Com o ambiente virtual ATIVO, instale as dependências

```bash
  python -m pip install -r .\requirements.txt
```

#### Após Instalado, verifique as alterações do models do Projeto

```bash
  python manage.py makemigrations
```
#### E logo, faça a migração

```bash
  python manage.py migrate
```

#### Crie um SuperUser

```bash
  python manage.py createsuperuser
```

#### Com o usuário Criado

```bash
  python manage.py runserver
```
