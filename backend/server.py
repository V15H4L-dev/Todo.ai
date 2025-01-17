from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from CRUD.authen import auth
import uvicorn

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]

app = FastAPI(docs_url="/api/docs", openapi_url="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth, prefix="/api")

if __name__ == "__main__": uvicorn.run("server:app", reload=True, port=8050, host='0.0.0.0')