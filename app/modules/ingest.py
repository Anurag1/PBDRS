import re
from app.core.logger import logger

class TextIngestor:
    def read_file(self, path): return open(path, 'r', encoding='utf-8').read()
    def tokenize(self, text):
        tokens = re.findall(r'\b\w+\b', text.lower())
        logger.info(f"Tokenized {len(tokens)} tokens")
        return tokens
