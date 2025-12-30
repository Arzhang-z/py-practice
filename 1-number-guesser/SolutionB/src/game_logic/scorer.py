class Scoree:
    def __init__(self,initial_score=100):
        self.score = initial_score
    
    def decrement(self,penalty=10):
        self.score -= penalty
    
    def total_score(self):
        return self.score
    