import numpy as np
from app.core.logger import logger
class EvaluationEngine:
    def compute_score(self, p):
        freq, ent = p.get("frequency",1), p.get("entropy",1)
        sem = p.get("semantic_cohesion", np.random.uniform(0.4,1))
        return round(0.4*np.log1p(freq)+0.4*(1-ent)+0.2*sem,4)
    def evaluate_all(self, patterns):
        scored = {pid:{**p,"score":self.compute_score(p)} for pid,p in patterns.items()}
        logger.info(f"Evaluated {len(scored)} patterns")
        return scored
