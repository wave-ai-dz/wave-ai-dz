# Simple rule-based hybrid controller using predicted wave height
class HybridController:
    def __init__(self):
        pass

    def decide_alpha(self, pred_H):
        """
        Decide how much of the generation goes to the OWC.
        alpha = fraction (0..1)
        - If wave height is high, prioritize OWC.
        - If low, prioritize Point Absorber.
        """
        if pred_H >= 2.0:
            return 0.8
        elif pred_H >= 1.0:
            return 0.5
        else:
            return 0.2
