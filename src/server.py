from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, ProdutoSimples
from src.schemas.schemas import Usuario, UsuarioSimples
from src.infra.sqlachemy.config.database import get_db, criar_bd
from src.infra.sqlachemy.repositories.repositorio_produto import RepositorioProduto
from src.infra.sqlachemy.repositories.repositorio_usuario import RepositorioUsuario


# criar_bd()

app = FastAPI()

# PRODUTOS
@app.post("/produtos", status_code=status.HTTP_201_CREATED)
def criar_produto(produto: Produto, session: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(session).criar(produto)
    return produto_criado


@app.get("/produtos", status_code=status.HTTP_200_OK, response_model=List[ProdutoSimples])
def listar_produtos(session: Session = Depends(get_db)):
    produtos = RepositorioProduto(session).listar()
    return produtos


@app.put("/produtos", response_model=Produto)
def atualizar_produto(produto: Produto, session: Session = Depends(get_db)):
    RepositorioProduto(session).editar(produto)
    return produto


@app.delete("/produtos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_produto(id: int, session: Session = Depends(get_db)):
    RepositorioProduto(session).remover(id)
    return



# USUÁRIOS

@app.post("/usuarios", status_code=status.HTTP_201_CREATED, response_model=Usuario)
def criar_usuario(usuario: Usuario, session: Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado


@app.get("/usuarios", status_code=status.HTTP_200_OK, response_model=List[Usuario])
def listar_usuarios(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios





