from fastapi import FastAPI

from app.routes.conversation import router

app = FastAPI(
    title="Personalized Networking Assistant API"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Backend is running successfully!"
    }