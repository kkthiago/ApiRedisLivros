<h1 align="center">📚 API de Livros</h1>

<p align="center">
  <em>Uma API RESTful construída com FastAPI, Redis e Docker Compose</em><br>
  <strong>CRUD completo com persistência de dados e documentação interativa</strong>
</p>

<p align="center">
  <!-- Badges -->
  <img src="https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge" alt="Versão">
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/python-3.9%2B-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/fastapi-0.111+-green?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/redis-database-red?style=for-the-badge&logo=redis" alt="Redis">
  <img src="https://img.shields.io/badge/docker-ready-0db7ed?style=for-the-badge&logo=docker" alt="Docker">
  <img src="https://img.shields.io/github/license/seu-usuario/seu-repositorio?style=for-the-badge" alt="Licença">
</p>

---

## ✨ Sobre o Projeto

Este projeto é uma **API REST** para realizar operações CRUD (Criar, Ler, Atualizar e Deletar) em uma coleção de livros.  
Ele demonstra o uso do **FastAPI** com **Redis** em um ambiente **containerizado com Docker Compose**.

### 🧩 Funcionalidades

✅ Listar todos os livros  
✅ Buscar livro por ID  
✅ Adicionar novo livro  
✅ Atualizar informações de livro existente  
✅ Deletar livro  
✅ Persistência de dados no Redis

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia            | Descrição                          |
| --------------------- | ---------------------------------- |
| 🐍 **Python 3.9+**    | Linguagem principal                |
| 🚀 **FastAPI**        | Framework web moderno e assíncrono |
| ⚙️ **Uvicorn**        | Servidor ASGI                      |
| 💾 **Redis**          | Banco de dados em memória          |
| 🐳 **Docker**         | Containerização                    |
| 📦 **Docker Compose** | Orquestração de contêineres        |

---

## 🚀 Como Rodar (Ambiente Docker Compose)

### 📋 Pré-requisitos

- Docker
- Docker Compose
- Git

### ⚙️ Instalação e Configuração

**1️⃣ Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

**2️⃣ Configure o ambiente:**

```bash
cp .env.example .env
```

> 💡 Os valores padrão de `.env.example` já são suficientes para rodar localmente.

**3️⃣ Suba os contêineres:**

```bash
docker-compose up --build
```

Acesse a API em:
👉 [http://localhost:8080](http://localhost:8080)
Documentação interativa (Swagger UI):
👉 [http://localhost:8080/docs](http://localhost:8080/docs)

---

## 📡 Endpoints da API

| Método   | Endpoint             | Descrição                                    |
| -------- | -------------------- | -------------------------------------------- |
| `GET`    | `/`                  | Retorna uma mensagem de boas-vindas          |
| `GET`    | `/livros`            | Lista todos os livros                        |
| `GET`    | `/livros/{livro_id}` | Retorna um livro específico                  |
| `POST`   | `/livros`            | Cria um novo livro                           |
| `PUT`    | `/livros/{livro_id}` | Atualiza informações de um livro             |
| `DELETE` | `/livros/{livro_id}` | Deleta um livro                              |
| `GET`    | `/debug/redis`       | Mostra todas as chaves e valores armazenados |

---

## 🧪 Exemplos de Uso (cURL)

### ➕ Criar um novo livro

```bash
curl -X 'POST' \
  'http://localhost:8080/livros' \
  -H 'Content-Type: application/json' \
  -d '{
    "titulo": "Duna",
    "author": "Frank Herbert"
  }'
```

### 📚 Listar todos os livros

```bash
curl -X 'GET' 'http://localhost:8080/livros'
```

### 🔍 Buscar um livro por ID

```bash
curl -X 'GET' 'http://localhost:8080/livros/SEU_LIVRO_ID'
```

### 🧠 Verificar cache no Redis

```bash
curl -X 'GET' 'http://localhost:8080/debug/redis'
```

### ✏️ Atualizar um livro

```bash
curl -X 'PUT' \
  'http://localhost:8080/livros/SEU_LIVRO_ID' \
  -H 'Content-Type: application/json' \
  -d '{
    "titulo": "Duna (Edição de Colecionador)"
  }'
```

### ❌ Deletar um livro

```bash
curl -X 'DELETE' 'http://localhost:8080/livros/SEU_LIVRO_ID'
```

---

## 🤝 Contribuição

Contribuições são muito bem-vindas!
Siga os passos abaixo para colaborar:

```bash
# 1. Faça um fork do projeto
# 2. Crie sua branch de feature
git checkout -b feature/nova-feature

# 3. Faça o commit das mudanças
git commit -m "Adiciona nova feature"

# 4. Envie para o repositório remoto
git push origin feature/nova-feature

# 5. Abra um Pull Request 🚀
```

---

## 🧠 Autor

👤 **Thiago Alves Soares**
💻 Desenvolvedor Python & FastAPI
