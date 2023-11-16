import time
import random
import numpy as np
from sklearn.ensemble import IsolationForest


class AnomalyDetector:
    data_stream = []

    def __init__(self, window_size=25) -> None:
        self.window_size = window_size
        self.model = IsolationForest(contamination=0.5)

    def generate_data_point(self) -> float:
        regular_pattern = 10 * (1+0.1*(time.time() % 10))
        seasonal_element = 5 * (1+0.5*(time.time() % 10))
        random_noise = random.gauss(0, 1)
        data_point = regular_pattern+seasonal_element+random_noise
        return data_point

    def detect_anomaly(self, data_point) -> str | float:
        if len(self.data_stream) > self.window_size:
            data = np.array(
                self.data_stream[-self.window_size:]).reshape(-1, 1)

            self.model.fit(data)
            anomaly_score = self.model.decision_function([[data_point]])

            if anomaly_score < 0:
                return data_point
            else:
                return 'N'

        else:
            return 'N'
