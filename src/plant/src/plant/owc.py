import numpy as np

# Simple quadratic relation: P = k1 * H^2
class OscillatingWaterColumn:
    def __init__(self, k1=30.0):
        self.k1 = k1

    def produce(self, H):
        return max(0.0, self.k1 * (H**2))
