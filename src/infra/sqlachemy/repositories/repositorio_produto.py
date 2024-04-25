from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlachemy.models import models


class RepositorioProduto():

    def __init__(self, db: Session):
        self.session = db

    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(
            nome=produto.nome,
            detalhes=produto.detalhes,
            preco=produto.preco,
            disponivel=produto.disponivel
        )
        self.session.add(db_produto)
        self.session.commit()
        self.session.refresh(db_produto)
        return db_produto

    def listar(self):
        produtos = self.session.query(models.Produto).all()
        return produtos

    def obter(self, produto_id: int):
        stmt = select(models.Produto).filter_by(id=produto_id)
        produto = self.session.execute(stmt).one()

        return produto

    def remover(self, produto_id: int):
        stmt = delete(models.Produto).where(models.Produto.id == produto_id)
        self.session.execute(stmt)
        self.session.commit()
