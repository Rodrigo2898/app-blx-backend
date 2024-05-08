from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlachemy.models import models
from typing import List


class RepositorioPedido():

    def __init__(self, db: Session):
        self.session = db

    def criar(self, pedido: schemas.Pedido):
        db_pedido = models.Pedido(
            quantidade=pedido.quantidade,
            local_entrega=pedido.local_entrega,
            tipo_entrega=pedido.tipo_entrega,
            observacoes=pedido.observacoes,
            usuario_id=pedido.usuario_id,
            produto_id=pedido.produto_id
        )
        self.session.add(db_pedido)
        self.session.commit()
        self.session.refresh(db_pedido)
        return db_pedido

    def listar(self):
        stmt = select(models.Pedido)
        pedidos = self.session.execute(stmt).scalars().all()

    def buscar_por_Id(self, id: int):
        consulta = select(models.Pedido).where(models.Pedido.id == id)
        pedido = self.session.execute(consulta).scalars().first()
        return pedido

    def listar_pedidos_por_usuario_id(self, usuario_id: int):
        pass

    def listar_minhas_vendas_por_usuario_id(self, usuario_id: int) -> List[models.Pedido]:
        pass
