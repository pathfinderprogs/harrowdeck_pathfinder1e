import csv
from bisect import bisect_left
import numpy as np

class RollTable:

    def __init__(self, options: np.array, weights: np.array) -> "RollTable":
        self.options = options
        self.weights = weights
        pdf = weights/np.sum(weights)
        self.cdf = np.cumsum(pdf)

    def get_item(self):
        roll = np.random.random()
        idx = bisect_left(self.cdf, roll)
        return self.options[idx]