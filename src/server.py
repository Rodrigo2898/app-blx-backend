from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import rotas_produtos, rotas_auth, rotas_pedidos

# criar_bd()

app = FastAPI()

# CORS

origins = [
    "http://localhost:3000",
    "https://myapp.vercel.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Rotas Proutos
app.include_router(rotas_produtos.router)

# Rotas Segurança: Autenticação e Autorização
app.include_router(rotas_auth.router, prefix="/auth")

# Rotas Pedidos
app.include_router(rotas_pedidos.router)





