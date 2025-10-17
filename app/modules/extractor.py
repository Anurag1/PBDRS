from collections import Counter
import numpy as np
from tqdm import tqdm
from app.core.logger import logger

class PatternExtractor:
    def __init__(self, min_support=3, max_length=8):
        self.min_support, self.max_length = min_support, max_length

    def extract(self, tokens):
        patterns = {}
        for n in tqdm(range(2, self.max_length+1), desc="Extracting"):
            ngrams = [tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1)]
            freq = Counter(ngrams)
            for seq, count in freq.items():
                if count >= self.min_support:
                    pid = f"P{len(patterns)+1:04d}"
                    patterns[pid] = {
                        "composition": seq,
                        "frequency": count,
                        "entropy": -sum((count/len(tokens))*np.log2(count/len(tokens))),
                        "level": n
                    }
        logger.info(f"Extracted {len(patterns)} patterns")
        return patterns
