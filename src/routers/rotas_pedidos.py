from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Pedido
from src.infra.sqlachemy.config.database import get_db
from src.infra.sqlachemy.repositories.repositorio_pedido import RepositorioPedido

router = APIRouter()

# PEDIDOS

@router.post("/pedidos", status_code=status.HTTP_201_CREATED, response_model=Pedido)
def fazer_pedidos(pedido: Pedido, session: Session = Depends(get_db)):
    pedido_criado = RepositorioPedido(session).criar(pedido)
    return pedido_criado


@router.get("/pedidos/{id}", response_model=Pedido)
def exibir_pedido(id: int, session: Session = Depends(get_db)):
    try:
        pedido_localizado = RepositorioPedido(session).buscar_por_Id(id)
        return pedido_localizado
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não existe o pedido com o id: {id}')

@router.get("/pedidos/{usuario_id}/compras", response_model=List[Pedido])
def listar_pedidos_por_usuario(usuario_id: int, session: Session = Depends(get_db)):
    pedidos = RepositorioPedido(session).listar_pedidos_por_usuario_id(usuario_id)
    return pedidos


@router.get("/pedidos/{usuario_id}/vendas", response_model=List[Pedido])
def listar_vendas_por_usuario(usuario_id: int, session: Session = Depends(get_db)):
    pedidos = RepositorioPedido(session).listar_minhas_vendas_por_usuario_id(usuario_id)
    return pedidos