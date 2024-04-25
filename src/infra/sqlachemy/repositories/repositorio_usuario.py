from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlachemy.models import models


class RepositorioUsuario():
    def __init__(self, db: Session):
        self.session = db

    def criar(self, usuario: schemas.UsuarioSimples):
        db_usuario = models.Usuario(
            nome=usuario.nome,
            telefone=usuario.telefone
        )
        self.session.add(db_usuario)
        self.session.commit()
        self.session.refresh(db_usuario)
        return db_usuario

    def listar(self):
        usuarios = self.session.query(models.Usuario).all()
        return usuarios