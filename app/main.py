from fastapi import FastAPI
from app.routes.validate import router as validate_router

app = FastAPI(title="FlowGuard API")

app.include_router(validate_router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "FlowGuard is running"}
