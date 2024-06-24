# MyProject

Este é um projeto básico do Django, criado para exibir uma mensagem "Hello, World!". Abaixo você encontrará instruções sobre como configurar, executar e entender a estrutura do projeto.

## Estrutura do Projeto


### Arquivos e Diretórios

- **manage.py**: Utilitário de linha de comando para interagir com o projeto Django (iniciar servidor, aplicar migrações, etc.).
- **myproject/** (diretório interno):
  - **__init__.py**: Indica que este diretório deve ser tratado como um pacote Python.
  - **settings.py**: Contém as configurações do projeto (banco de dados, aplicativos instalados, middleware, etc.).
  - **urls.py**: Arquivo de roteamento de URLs do projeto.
  - **asgi.py**: Configuração para servidores compatíveis com ASGI (comunicação assíncrona).
  - **wsgi.py**: Configuração para servidores compatíveis com WSGI (comunicação síncrona).
- **hello/** (diretório da aplicação):
  - **__init__.py**: Indica que este diretório deve ser tratado como um pacote Python.
  - **admin.py**: Configurações para a interface de administração do Django.
  - **apps.py**: Configurações da aplicação.
  - **migrations/**: Diretório para armazenar migrações do banco de dados.
  - **models.py**: Definição dos modelos da aplicação.
  - **tests.py**: Testes da aplicação.
  - **views.py**: Views da aplicação (funções que retornam respostas HTTP).
  - **urls.py**: Arquivo de roteamento de URLs da aplicação.

## Configuração

### Pré-requisitos

- Python 3.x
- Django (versão utilizada no projeto)

### Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/Marcos-Meireles/Hello_Django.git
    cd myproject
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```bash
    pip install django
    ```

## Executando o Projeto

1. Aplique as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

2. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

3. Acesse a aplicação no navegador:

    Abra o navegador e vá para `http://127.0.0.1:8000/hello/`. Você verá a mensagem "Hello, World!".

## Explicação das Views

No arquivo `hello/views.py`, há uma função simples que retorna uma resposta HTTP com a mensagem "Hello, World!".

```python
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")
from django.urls import path
from .views import hello_world

urlpatterns = [
    path('', hello_world, name='hello_world'),
]
```



Este arquivo README.md fornece uma visão geral do projeto, explicando a estrutura dos diretórios e arquivos, além de fornecer instruções detalhadas sobre como configurar e executar o projeto.
