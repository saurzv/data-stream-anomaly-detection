import time
import random
import logging
import numpy as np
from sklearn.ensemble import IsolationForest

logger = logging.getLogger(__name__)


class AnomalyDetector:
    data_stream = []

    def __init__(self, window_size=25) -> None:
        """
        Initializes a new instance of the class.

        Args:
            window_size (int, optional): The size of the window. Defaults to 25.

        Returns:
            None
        """
        self.window_size = window_size
        self.model = IsolationForest(contamination=0.5)

    def generate_data_point(self) -> float:
        """
        Generate a data point based on a combination of regular pattern, seasonal element, and random noise.

        Returns:
            float: The generated data point.
        """
        regular_pattern = 10 * (1+0.1*(time.time() % 10))
        seasonal_element = 5 * (1+0.5*(time.time() % 10))
        random_noise = random.gauss(0, 1)
        data_point = regular_pattern + seasonal_element + random_noise
        return data_point

    def detect_anomaly(self, data_point: float) -> str | float:
        """
        Detects anomalies in a data stream.

        Args:
            data_point (float): The data point to be checked for anomaly.

        Returns:
            str | float: Returns either the data point itself if it is an anomaly or 'N' if it is not.
        """
        if len(self.data_stream) > self.window_size:
            data = np.array(
                self.data_stream[-self.window_size:]).reshape(-1, 1)

            self.model.fit(data)
            anomaly_score = self.model.decision_function([[data_point]])

            if anomaly_score < 0:
                logger.info(
                    f'\nData Point    :   {data_point}\nAnomaly Score :   {anomaly_score}\n')
                return data_point
            else:
                return 'N'

        else:
            return 'N'
