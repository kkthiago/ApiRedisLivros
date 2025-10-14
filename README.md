# 📚 API de Livros

\<div align="center"\>

\</div\>

Uma API RESTful construída com Python e FastAPI para gerenciar uma biblioteca virtual, utilizando Redis para cache.

## ✨ Sobre o Projeto

Este projeto é uma API para realizar operações CRUD (Criar, Ler, Atualizar, Deletar) em uma coleção de livros. É uma demonstração prática do uso de FastAPI para criar APIs rápidas e eficientes.

### Principais Funcionalidades:

- ✅ Listar todos os livros.
- ✅ Buscar um livro específico por ID.
- ✅ Adicionar um novo livro.
- ✅ Atualizar informações de um livro existente.
- ✅ Deletar um livro.

### 🛠️ Tecnologias Utilizadas:

- 🐍 **[Python 3.9+](https://www.python.org/)**
- 🚀 **[FastAPI](https://fastapi.tiangolo.com/)**
- ⚙️ **[Uvicorn](https://www.uvicorn.org/)**
- 💾 **[Redis](https://redis.io/)**
- 🧪 **[Pytest](https://docs.pytest.org/)**

---

## 🚀 Começando

Siga estas instruções para ter uma cópia do projeto rodando na sua máquina local para desenvolvimento e testes.

### Pré-requisitos

- **Python 3.9** ou superior.
- **Redis** instalado e em execução.
- Um gerenciador de pacotes como `pip`.

### ⚙️ Instalação

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

4.  **Inicie o servidor da API:**

    ```sh
    uvicorn main:app --reload
    ```

5.  A API estará disponível em `http://localhost:8080`.

6.  Acesse a documentação interativa (Swagger UI) em `http://localhost:8080/docs`.

---

## 📡 Endpoints da API

A API segue os padrões REST e utiliza JSON para as requisições e respostas.

#### `GET /`

Retorna uma mensagem de boas-vindas.

- 📤 **Resposta (200 OK):**
  ```json
  {
    "message": "Bem-vindo à API da Biblioteca."
  }
  ```

#### `GET /todoslivros`

Retorna uma lista de todos os livros cadastrados.

- 📤 **Resposta (200 OK):**
  ```json
  [
    {
      "livro_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
      "titulo": "O Guia do Mochileiro das Galáxias",
      "author": "Douglas Adams"
    }
  ]
  ```

#### `GET /livro/{livro_id}`

Retorna os detalhes de um livro específico.

- 📥 **Parâmetros:** `livro_id` (UUID)
- 📤 **Resposta (200 OK):**
  ```json
  {
    "livro_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
    "titulo": "O Guia do Mochileiro das Galáxias",
    "author": "Douglas Adams"
  }
  ```

#### `POST /livro`

Cria um novo livro.

- 📥 **Corpo da Requisição:**
  ```json
  {
    "titulo": "Duna",
    "author": "Frank Herbert"
  }
  ```
- 📤 **Resposta (200 OK):** Retorna a lista completa de livros, incluindo o recém-criado.

#### `PUT /atualizarlivro/{livro_id}`

Atualiza os detalhes de um livro existente.

- 📥 **Parâmetros:** `livro_id` (UUID)
- 📥 **Corpo da Requisição (apenas os campos a serem alterados):**
  ```json
  {
    "titulo": "Duna (Edição Revisada)"
  }
  ```
- 📤 **Resposta (200 OK):** Retorna o objeto do livro com os dados atualizados.

#### `DELETE /deletarlivro/{livro_id}`

Deleta um livro do acervo.

- 📥 **Parâmetros:** `livro_id` (UUID)
- 📤 **Resposta (200 OK):**
  ```json
  {
    "message": "O livro \"Duna\" foi deletado com sucesso!"
  }
  ```

---

## 🧪 Testes

Para garantir a qualidade e o funcionamento correto da API, os testes foram escritos com `pytest`.

1.  **Instale as dependências de desenvolvimento:**
    ```sh
    pip install -r requirements-dev.txt
    ```
2.  **Execute os testes:**
    ```sh
    pytest tests/
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
