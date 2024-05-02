from pydantic import BaseModel
from typing import Optional, List


# Essa arquivo schemas é usado apenas para requests e responses

class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str

    class Config:
        orm_mode = True


class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str

    class Config:
        orm_mode = True


class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: int
    # usuario: Optional[Usuario]

    class Config:
        orm_mode = True


class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    usuario: Optional[Usuario]

    class Config:
        orm_mode = True


class Pedido(BaseModel):
    id: Optional[int] = None
    quantidade: int
    entrega: bool = True
    endereco: str
    onservacoes: Optional[str] = "Sem observações"
