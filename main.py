## Importações
import json
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import redis
from uuid import UUID, uuid4
import os


##PRÉ CONFIGURAÇÕES##
## Defnição do APP, utilização para as routes e metodos do FASTAPI e suas rotas
app = FastAPI(
  title="API de Livros",
  description="API para gerenciar uma bibilioteca virtual",
  version="1.0.0",
)

## Defnição do cliente redis, para ter acesso a seus "caches"
redis_client = redis.asyncio.Redis(host=os.getenv('REDIS_HOST'), port=int(os.getenv('REDIS_PORT')), decode_responses=True)

## Modelo/Classe para atualização de itens
class LivroUpdate(BaseModel):
    titulo: Optional[str] = None
    author: Optional[str] = None

## Modelo/Classe para itens (livros) com ID (universalmente único), título e autor
class Livro(BaseModel):
    livro_id: UUID = Field(default_factory=uuid4)
    titulo: str
    author: str

## Função de cache para salvar livros, para reutilização futura
async def salvar_livros_redis(livro_id: UUID, livro: Livro):
  await redis_client.set(f"livros:{livro_id}", json.dumps(livro.model_dump()))

## Função de cache para deletar livros, para reutilização futura
async def deletar_livro_redis(livro_id: UUID):
  await redis_client.delete(f"livros:{livro_id}")


## ROUTES ##
## GET, Tela de home para API
@app.get("/")
def root():
  return {"message": "Bem-vindo à API da Biblioteca."}

## GET, Listar todos os livros disponíveis
@app.get("/livros", response_model=list[Livro])
async def listar_livros():
  keyList = await redis_client.keys("livros:*")
  livros = []
  for key in keyList:
    value = await redis_client.get(key)
    livro_dict = json.loads(value)
    livros.append(livro_dict)
  if not livros:
    raise HTTPException(status_code=404,detail="Não há livros registrados. Tente adicionar algum.")
  else:
    return livros
  
## GET, Listar livro específico por id respectivo
@app.get("/livros/{livro_id}", response_model=Livro)
async def get_livro(livro_id: UUID):
  livro_data = await redis_client.get(f"livros:{livro_id}")
  if livro_data:
    return json.loads(livro_data)
  else:
    raise HTTPException(status_code=404, detail=f'Livro Id "{livro_id}" não encontrado. Tente novamente.')

## GET, DEBUG do Redis, lista todos livros listados
@app.get("/debug/redis")
async def ver_livros_redis():
  keyList = await redis_client.keys("livros:*")
  livros = []
  
  for key in keyList:
    value = await redis_client.get(key)
    livros.append({"key": key, "value": json.loads(value)})
  return livros

## POST, Criação de livro
@app.post("/livros")
async def create_livro(livro: Livro):
  
  await salvar_livros_redis(livro.livro_id,livro)
  return livro

## PUT, Atualização de livro
@app.put("/livros/{livro_id}", response_model= Livro)
async def atualizar_livro(livro_id: UUID, livro_update_data: LivroUpdate):
  livro = await redis_client.get(f"livros:{livro_id}")
  if not livro:
    raise HTTPException(status_code=404, detail=f"Livro com ID {livro_id} não encontrado. Tente novamente.")
  livro_data = json.loads(livro)
  
  update_data = livro_update_data.model_dump(exclude_unset=True)
  livro_data.update(update_data)
  
  livro_atualizado = Livro(**livro_data)
  await salvar_livros_redis(livro_id, livro_atualizado)

  return livro_atualizado
  
## DELETE, Deletar livros
@app.delete("/livros/{livro_id}")
async def delete_livro(livro_id: UUID):
  livro = await redis_client.get(f"livros:{livro_id}")
  if livro:
    await deletar_livro_redis(livro_id)
  else:
    raise HTTPException(status_code=404, detail=f"Livro com ID {livro_id} não encontrado. Tente novamente.")
  
  