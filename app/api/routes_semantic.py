from fastapi import APIRouter
from app.modules.semantic_engine import SemanticEngine
from app.modules.storage import PatternStorage

router = APIRouter()
storage = PatternStorage()
sem = SemanticEngine()

@router.get("/similar/{pid}")
def similar(pid:str):
    pats = storage.get_all(); emb = sem.encode_patterns(pats)
    return sem.find_similar(pats, emb, pid)

@router.get("/clusters")
def clusters(n:int=5):
    pats = storage.get_all(); emb = sem.encode_patterns(pats)
    labels = sem.cluster_patterns(emb,n)
    return {"clusters":[{"pid":pid,"cluster":int(l)} for pid,l in zip(pats.keys(),labels)]}
