import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.generated.register import register
from .movies_service import ProManServices

app = FastAPI()

register(app, prompt_api=ProManServices())

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def start() -> None:
    uvicorn.run(
        "src.fern_fastapi_starter.server:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
    )

@app.get("/")
async def read_root():
    return {"message": "Welcome to the API"}

if __name__ == "__main__":
    start()
