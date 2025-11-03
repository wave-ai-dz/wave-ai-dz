# Very simple AI-like predictor: moving average of recent wave heights
class WavePredictor:
    def __init__(self, window=5):
        self.window = window  # number of previous values to average

    def predict(self, history):
        if len(history) == 0:
            return 0.0
        # average of last N wave heights
        return sum(history[-self.window:]) / min(len(history), self.window)
