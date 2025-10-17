from app.core.logger import logger
class PatternStorage:
    def __init__(self): self.patterns = {}
    def store(self, new_patterns):
        self.patterns.update(new_patterns)
        logger.info(f"Stored {len(new_patterns)} patterns (total {len(self.patterns)})")
    def get_all(self): return self.patterns
    def get_top(self, n=10):
        return sorted(self.patterns.items(), key=lambda x: x[1]["frequency"], reverse=True)[:n]
