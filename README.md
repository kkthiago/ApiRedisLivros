# 📚 API de Livros

Uma API RESTful construída com Python e FastAPI para gerenciar uma biblioteca virtual, utilizando Redis como cache para otimizar as consultas.

## ✨ Sobre o Projeto

Este projeto é uma API para realizar operações CRUD (Criar, Ler, Atualizar, Deletar) em uma coleção de livros. É uma demonstração prática do uso de FastAPI para criar APIs rápidas, eficientes e assíncronas.

### Principais Funcionalidades:

- ✅ Listar todos os livros.
- ✅ Buscar um livro específico por ID.
- ✅ Adicionar um novo livro.
- ✅ Atualizar informações de um livro existente.
- ✅ Deletar um livro.
- ✅ Cache de dados em Redis para performance.

### 🛠️ Tecnologias Utilizadas:

- 🐍 **[Python 3.9+](https://www.python.org/)**
- 🚀 **[FastAPI](https://fastapi.tiangolo.com/)**
- ⚙️ **[Uvicorn](https://www.uvicorn.org/)**
- 💾 **[Redis](https://redis.io/)**
- 🐳 **[Docker](https://www.docker.com/)** (Opcional, para o Redis)

---

## 🚀 Começando

Siga estas instruções para ter uma cópia do projeto rodando na sua máquina local para desenvolvimento e testes.

### Pré-requisitos

- **Python 3.9** ou superior.
- **Git** para clonar o repositório.
- Um gerenciador de pacotes como `pip`.
- **Redis** ou **Docker** em execução.

### ⚙️ Instalação e Configuração

1.  **Clone o repositório:**

    ```sh
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2.  **Crie e ative um ambiente virtual:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use: `venv\Scripts\activate`
    ```

3.  **Instale as dependências:**

    ```sh
    pip install -r requirements.txt
    ```

4.  **Configure e inicie o Redis:**

    Você precisa de uma instância do Redis rodando na porta padrão (`6379`). A forma mais fácil é usando Docker.

    **Opção 1: Docker (Recomendado)**
    Se você tem Docker instalado, execute o seguinte comando no seu terminal:

    ```sh
    docker run --name redis-livros -p 6379:6379 -d redis
    ```

    Isso irá baixar a imagem do Redis e iniciar um contêiner em segundo plano.

    **Opção 2: Instalação Local**
    Se preferir, instale o Redis diretamente no seu sistema operacional. Siga as instruções no [site oficial do Redis](https://www.google.com/search?q=https://redis.io/docs/getting-started/installation/).

5.  **Inicie o servidor da API:**

    ```sh
    uvicorn main:app --reload --port 8000
    ```

6.  A API estará disponível em `http://localhost:8000`.

7.  Acesse a documentação interativa (Swagger UI) em `http://localhost:8000/docs`.

---

## 📡 Endpoints da API

A API segue os padrões REST e utiliza JSON para as requisições e respostas.

#### `GET /`

Retorna uma mensagem de boas-vindas.

#### `GET /livros`

Retorna uma lista de todos os livros cadastrados.

#### `GET /livros/{livro_id}`

Retorna os detalhes de um livro específico.

#### `POST /livros`

Cria um novo livro. O livro criado também é salvo no cache do Redis.

#### `PUT /livros/{livro_id}`

Atualiza os detalhes de um livro existente. A atualização também é refletida no cache.

#### `DELETE /livros/{livro_id}`

Deleta um livro. O registro correspondente também é removido do cache.

#### `GET /debug/redis`

Endpoint de depuração para visualizar todas as chaves de livros atualmente no cache do Redis.

---

### 🧪 Exemplos de Uso com cURL

Abra um terminal e use os comandos `cURL` abaixo para interagir com a API.

1.  **Criar um novo livro:**

    ```sh
    curl -X 'POST' \
      'http://localhost:8000/livros' \
      -H 'Content-Type: application/json' \
      -d '{
        "titulo": "Duna",
        "author": "Frank Herbert"
      }'
    ```

    _Anote o `livro_id` retornado para usar nos próximos passos._

2.  **Listar todos os livros:**

    ```sh
    curl -X 'GET' 'http://localhost:8000/livros'
    ```

3.  **Buscar um livro específico por ID:**
    _(Substitua `SEU_LIVRO_ID` pelo ID que você anotou)_

    ```sh
    curl -X 'GET' 'http://localhost:8000/livros/SEU_LIVRO_ID'
    ```

4.  **Verificar o cache do Redis:**
    _(Você verá a chave `livro:SEU_LIVRO_ID` que foi criada)_

    ```sh
    curl -X 'GET' 'http://localhost:8000/debug/redis'
    ```

5.  **Atualizar um livro:**
    _(Substitua `SEU_LIVRO_ID` pelo ID que você anotou)_

    ```sh
    curl -X 'PUT' \
      'http://localhost:8000/livros/SEU_LIVRO_ID' \
      -H 'Content-Type: application/json' \
      -d '{
        "titulo": "Duna (Edição de Colecionador)"
      }'
    ```

6.  **Deletar um livro:**
    _(Substitua `SEU_LIVRO_ID` pelo ID que você anotou)_

    ```sh
    curl -X 'DELETE' 'http://localhost:8000/livros/SEU_LIVRO_ID'
    ```

---

## 🤝 Contribuição

Contribuições são o que tornam a comunidade de código aberto um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será **muito apreciada**.

1.  Faça um _Fork_ do projeto.
2.  Crie sua _Feature Branch_ (`git checkout -b feature/AmazingFeature`).
3.  Faça o _Commit_ de suas alterações (`git commit -m 'Add some AmazingFeature'`).
4.  Faça o _Push_ para a _Branch_ (`git push origin feature/AmazingFeature`).
5.  Abra um _Pull Request_.

---

## 📝 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
