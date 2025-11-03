import numpy as np

# Simple linear relation: P = k2 * H
class PointAbsorber:
    def __init__(self, k2=50.0):
        self.k2 = k2  # kW per meter (example)

    def produce(self, H):
        # ensure non-negative
        return max(0.0, self.k2 * H)
