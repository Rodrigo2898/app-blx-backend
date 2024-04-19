from pydantic import BaseModel
from typing import Optional, List

# Essa arquivo schemas é usado apenas para requests e responses
class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    # meus_produtos: List[Produto]
    # minhas_vendas: List[Pedido]
    # meus_pedidos: List[Pedido]


class Produto(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

    orm_mode = True


class Pedido(BaseModel):
    id: Optional[str] = None
    usuario: Usuario
    produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    onservacoes: Optional[str] = "Sem observações"
