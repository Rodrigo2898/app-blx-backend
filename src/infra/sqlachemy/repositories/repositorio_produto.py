from sqlalchemy import select, delete, update
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
            disponivel=produto.disponivel,
            usuario_id=produto.usuario_id
        )
        self.session.add(db_produto)
        self.session.commit()
        self.session.refresh(db_produto)
        return db_produto

    def listar(self):
        produtos = self.session.query(models.Produto).all()
        return produtos

    def buscar_por_Id(self, id: int):
        consulta = select(models.Produto).where(models.Produto.id == id)
        produto = self.session.execute(consulta).scalars().first()
        return produto

    def editar(self, id: int, produto: schemas.Produto):
        update_stmt = update(models.Produto).where(models.Produto.id == id).values(
                                                                        nome=produto.nome,
                                                                        detalhes=produto.detalhes,
                                                                        preco=produto.preco,
                                                                        disponivel=produto.disponivel)

        self.session.execute(update_stmt)
        self.session.commit()

    def remover(self, produto_id: int):
        delete_stmt = delete(models.Produto).where(models.Produto.id == produto_id)
        self.session.execute(delete_stmt)
        self.session.commit()
