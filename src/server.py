from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from src.routers import rotas_produtos, rotas_auth, rotas_pedidos
from src.jobs.write_notification import write_notification

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


@app.post('/send_email/{email}')
def send_email(email: str, background: BackgroundTasks):
    background.add_task(write_notification, email, 'Opa, tudo bem')
    return {'Ok': 'Mensagem enviada'}

# Middlewares
@app.middleware('http')
async def processar_tempo_requisicao(request: Request, next):
    print('Interceptou chegada...')

    response = await next(request)

    print('Interceptou a volta...')

    return response
