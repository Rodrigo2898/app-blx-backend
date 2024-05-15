from pydantic import BaseModel
from typing import Optional, List


# Essa arquivo schemas é usado apenas para requests e responses


class ProdutoSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    preco: float
    disponivel: bool

    class Config:
        orm_mode = True

class PedidoSimplesListar(BaseModel):
    id: Optional[int] = None
    quantidade: int
    local_entrega: Optional[str] = None
    tipo_entrega: str
    observacao: Optional[str] = "Sem observações"

    class Config:
        orm_mode = True


class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str
    produtos: List[ProdutoSimples] = []
    pedidos: List[PedidoSimplesListar] = []

    class Config:
        orm_mode = True


class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str

    class Config:
        orm_mode = True


class LoginData(BaseModel):
    senha: str
    telefone: str


class LoginSucesso(BaseModel):
    usuario: UsuarioSimples
    access_token: str


class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: Optional[int] = None
    usuario: Optional[UsuarioSimples] = None

    class Config:
        orm_mode = True


class Pedido(BaseModel):
    id: Optional[int] = None
    quantidade: int
    local_entrega: Optional[str] = None
    tipo_entrega: str
    observacao: Optional[str] = "Sem observações"
    usuario_id: Optional[int] = None
    produto_id: Optional[int] = None

    class Config:
        orm_mode = True


class PedidoSimples(BaseModel):
    id: Optional[int] = None
    quantidade: int
    local_entrega: Optional[str] = None
    tipo_entrega: str
    observacao: Optional[str] = "Sem observações"
    usuario_id: Optional[int]
    produto_id: Optional[int]

    usuario: Optional[UsuarioSimples] = None
    produto: Optional[ProdutoSimples] = None

    class Config:
        orm_mode = True