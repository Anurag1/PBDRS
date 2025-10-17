class RewardEngine:
    def __init__(self, threshold=0.6, decay=0.05):
        self.threshold, self.decay = threshold, decay
    def reinforce(self, patterns):
        for p in patterns.values():
            s = p.get("score",0)
            if s>=self.threshold: p["frequency"]+=1; p["reward"]="reinforced"
            else: p["frequency"]=max(1,p["frequency"]*(1-self.decay)); p["reward"]="weakened"
        return patterns
