from fastapi import FastAPI
from app.api import (
    routes_patterns, routes_semantic, routes_reasoner,
    routes_feedback, routes_health
)
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

app.include_router(routes_patterns.router, prefix="/patterns", tags=["Patterns"])
app.include_router(routes_semantic.router, prefix="/semantic", tags=["Semantic"])
app.include_router(routes_reasoner.router, prefix="/reasoner", tags=["Reasoning"])
app.include_router(routes_feedback.router, prefix="/feedback", tags=["Feedback"])
app.include_router(routes_health.router, prefix="/health", tags=["Health"])

@app.get("/")
def root():
    return {"message": "Pattern-Based Data Representation System is running 🚀"}
