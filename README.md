# 📚 Biblioteca Django

Projeto de estudo desenvolvido com Django para praticar os fundamentos do framework por meio de um sistema simples de biblioteca.

A aplicação permite organizar livros por categoria, associar registros a usuários e acompanhar empréstimos e devoluções.

## Funcionalidades

- Cadastro de livros
- Cadastro de categorias
- Cadastro de usuários
- Registro de empréstimos
- Controle de devolução
- Avaliação do estado do livro após o empréstimo
- Upload de capa dos livros

## Tecnologias e conceitos praticados

- Python
- Django
- Django ORM
- SQLite
- Templates Django
- Forms e views
- Relacionamentos entre models
- Migrations
- Upload de arquivos com `ImageField`

## Estrutura principal

```text
Biblioteca-Django/
├── biblioteca/   # configurações do projeto Django
├── livro/        # livros, categorias e empréstimos
├── usuarios/     # cadastro de usuários
├── templates/    # templates da aplicação
└── manage.py
```

## Executando localmente

Este é um projeto antigo de estudo e as dependências não estão versionadas em um arquivo de lock/requirements. Dependendo da versão do Python, pode ser necessário utilizar uma versão compatível do Django.

Exemplo de configuração:

```bash
python -m venv .venv
source .venv/bin/activate
pip install django pillow
python manage.py migrate
python manage.py runserver
```

No Windows, a ativação do ambiente virtual pode ser feita com:

```bash
.venv\Scripts\activate
```

Depois, acesse:

```text
http://127.0.0.1:8000/
```

## Observação sobre o projeto

Este repositório representa uma etapa inicial do meu aprendizado com Django e foi mantido público para mostrar minha evolução como desenvolvedor.

Algumas decisões presentes no código — especialmente autenticação própria, tratamento de credenciais e organização da aplicação — não representam os padrões que utilizo atualmente em projetos profissionais.

Para uma referência mais atual do meu trabalho com Django, APIs REST, React, Docker e PostgreSQL, veja o projeto [GuteBurguer](https://github.com/AlisonBaade/GuteBurguer).
