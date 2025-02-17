# app/main.py
from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="PDF Uploader API")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
