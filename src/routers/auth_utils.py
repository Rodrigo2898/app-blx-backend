from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session
from src.infra.sqlachemy.config.database import get_db
from src.infra.providers import token_provider
from src.infra.sqlachemy.repositories.repositorio_usuario import RepositorioUsuario

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')


def obter_usuario_logado(token: str =  Depends(oauth2_schema),
                         session: Session = Depends(get_db)):
    # Decodificar o token, pegar o telefone, buscar o usuario no bd e retornar
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token inválido')
    try:
        telefone = token_provider.verificar_access_token(token)
    except JWTError as e:
        raise exception

    if not telefone:
        raise exception

    usuario = RepositorioUsuario(session).obter_por_telefone(telefone)

    if not usuario:
        raise exception

    return usuario
