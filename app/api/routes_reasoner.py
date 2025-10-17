from fastapi import APIRouter, Query
from app.modules.neural_reasoner import NeuralReasoner
from app.modules.storage import PatternStorage

router = APIRouter()
storage = PatternStorage()
reasoner = NeuralReasoner()

@router.get("/predict")
def predict(context: str = Query(...)):
    return {"predicted": reasoner.predict_next_pattern(context)}

@router.post("/evolve")
def evolve(num_new:int=3):
    pats = storage.get_all()
    return {"evolved": reasoner.evolve_patterns(pats,num_new)}
