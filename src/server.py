from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto
from src.infra.sqlachemy.config.database import get_db
from src.infra.sqlachemy.repositories.produto import RepositorioProduto


app = FastAPI()


@app.get("/produtos")
def listar_produtos(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@app.post("/produtos")
def cria_produtos():
    return {"mensagem": "Criando Produtos"}
