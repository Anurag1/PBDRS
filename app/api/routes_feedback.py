from fastapi import APIRouter
from app.modules.storage import PatternStorage
from app.modules.evaluation_engine import EvaluationEngine
from app.modules.reward_engine import RewardEngine

router = APIRouter()
storage = PatternStorage(); evaluator = EvaluationEngine(); rewarder = RewardEngine()

@router.post("/cycle")
def feedback_cycle():
    pats = storage.get_all()
    scored = evaluator.evaluate_all(pats)
    updated = rewarder.reinforce(scored)
    storage.store(updated)
    return {"patterns": len(updated)}
