import json
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import redis
from uuid import UUID, uuid4

app = FastAPI(
  title="API de Livros",
  description="API para gerenciar uma bibilioteca virtual",
  version="1.0.0",
)

redis_client = redis.Redis(host='localgost', port=6379, decode_responses=True)

class LivroUpdate(BaseModel):
    titulo: Optional[str] = None
    author: Optional[str] = None
    
class Livro(BaseModel):
    livro_id: UUID = Field(default_factory=uuid4)
    titulo: str
    author: str
  
biblioteca = []

async def salvar_livros_redis(livro_id: UUID, livro: Livro):
  redis_client.set(f"livro:{livro_id}", json.dumps(livro.dict()))
  
async def deletar_livro_redis(livro_id: UUID):
  redis_client.delete(f"livro:{livro_id}")

@app.get("/")
def root():
  return {"message": "Bem-vindo à API da Biblioteca."}

@app.get("/todoslivros", response_model=list[Livro])
def listar_livros(limit = 10):
  if biblioteca:
    return biblioteca[0:limit]
  else: 
    raise HTTPException(status_code=404, detail="Não há nenhum livro na lista!")
  
@app.get("/livro/{livro_id}", response_model=Livro)
def get_livro(livro_id: UUID): 
    for livro in biblioteca:
        if livro.livro_id == livro_id:
            return livro
    raise HTTPException(status_code=404, detail=f'Livro Id "{livro_id}" não encontrado.')

@app.get("/debug/redis")
def ver_livros_redis():
  keyList = redis_client.keys("livros:*")
  livros = []
  
  for key in keyList:
    value = redis.client.get(key)
    livros.append({"key": key, "value": json.loads(value)})
  return livros

@app.post("/livro")
def create_livro(livro: Livro):
  biblioteca.append(livro)
  
  salvar_livros_redis(livro.livro_id,livro)
  return biblioteca
  
@app.put("/atualizarlivro/{livro_id}", response_model= Livro)
def atualizar_livro(livro_id: UUID, livro_update_data: LivroUpdate):
  livro_encontrado = None
  for livro_item in biblioteca:
    if livro_item.livro_id == livro_id:
      livro_encontrado = livro_item
      break
  if not livro_encontrado:
    raise HTTPException(status_code=404, detail=f"Livro com ID {livro_id} não encontrado.")
  
  update_data = livro_update_data.model_dump(exclude_unset=True)
  
  for key, value in update_data.items():
    setattr(livro_encontrado, key, value)
    
  return livro_encontrado
  
@app.delete("/deletarlivro/{livro_id}")
def delete_livro(livro_id: UUID):
  livro_a_deletar = None
  if biblioteca:
    for livro_item in biblioteca:
      if livro_item.livro_id == livro_id:
        livro_a_deletar = livro_item
    if livro_a_deletar:
      biblioteca.remove(livro_a_deletar)
      deletar_livro_redis(livro_id)
      return{"message": f'O livro "{livro_a_deletar.titulo}" foi deletado com sucesso!'}
    else:
      raise HTTPException(status_code=404, detail=f"Livro com ID {livro_id} não foi encontrado!")
  else:
    raise HTTPException(status_code=404, detail="Não há nenhum livro cadastrado na biblioteca.")