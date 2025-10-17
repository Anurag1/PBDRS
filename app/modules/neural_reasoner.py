import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from app.core.logger import logger

class NeuralReasoner:
    def __init__(self, model_name="gpt2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def predict_next_pattern(self, context, max_length=40):
        inputs = self.tokenizer(context, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=max_length, temperature=0.8, top_p=0.9)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def evolve_patterns(self, pattern_dict, num_new=3):
        text = " ".join([" ".join(p["composition"]) for p in pattern_dict.values()][:3])
        new_text = self.predict_next_pattern(text)
        new_seqs = [tuple(seq.split()) for seq in new_text.split(".") if seq.strip()]
        evolved = {f"E{i+1:04d}": {"composition": seq, "frequency": 1, "level": len(seq)} for i, seq in enumerate(new_seqs[:num_new])}
        logger.info(f"Evolved {len(evolved)} new patterns")
        return evolved
