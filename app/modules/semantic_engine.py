from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import numpy as np
from app.core.logger import logger

class SemanticEngine:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def encode_patterns(self, pattern_dict):
        texts = [" ".join(p["composition"]) for p in pattern_dict.values()]
        embeddings = self.model.encode(texts, show_progress_bar=True)
        logger.info(f"Encoded {len(texts)} patterns.")
        return embeddings

    def find_similar(self, pattern_dict, embeddings, target_pid, top_k=5):
        pids = list(pattern_dict.keys())
        idx = pids.index(target_pid)
        sims = cosine_similarity([embeddings[idx]], embeddings)[0]
        return sorted(zip(pids, sims), key=lambda x: x[1], reverse=True)[1:top_k+1]

    def cluster_patterns(self, embeddings, n_clusters=5):
        labels = KMeans(n_clusters=n_clusters, random_state=42).fit_predict(embeddings)
        logger.info(f"Clustered into {n_clusters} groups")
        return labels
