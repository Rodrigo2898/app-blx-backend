from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, ProdutoSimples
from src.schemas.schemas import UsuarioSimples
from src.infra.sqlachemy.config.database import get_db, criar_bd
from src.infra.sqlachemy.repositories.repositorio_produto import RepositorioProduto
from src.infra.sqlachemy.repositories.repositorio_usuario import RepositorioUsuario


criar_bd()

app = FastAPI()


@app.post("/produtos", status_code=status.HTTP_201_CREATED)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get("/produtos", status_code=status.HTTP_200_OK, response_model=List[ProdutoSimples])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos



@app.get("/usuarios")
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios


@app.post("/usuarios")
def criar_usuario(usuario: UsuarioSimples, db: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(db).criar(usuario)
    return usuario_criado

