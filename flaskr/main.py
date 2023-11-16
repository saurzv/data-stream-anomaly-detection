import time
import json
from . import data_stream
from flask import (
    Blueprint, Response, stream_with_context, render_template
)

detector = data_stream.AnomalyDetector()

bp = Blueprint("flaskr", __name__)


@bp.route('/')
def index():
    """
    A function that serves as the index route for the application.

    Returns:
        A rendered HTML template for the index page.
    """
    return render_template('index.html')


@bp.route('/data')
def dump_data():
    """
    Generates a data stream by continuously generating and detecting data points.

    Returns:
        A generator that yields data in the form of JSON strings.
    """
    def simulate_data_stream():
        """
        Simulates a data stream by continuously generating and detecting data points.

        Returns:
            A generator that yields data in the form of JSON strings.
        """
        i = -1
        while True:
            i += 1
            data_point = detector.generate_data_point()
            detector.data_stream.append(data_point)
            anomaly = detector.detect_anomaly(data_point)
            if anomaly == 'N':
                json_data = json.dumps({'key': i, 'value': [data_point]})
            else:
                json_data = json.dumps(
                    {'key': i, 'value': [data_point, anomaly]})

            yield f"data:{json_data}\n\n"
            time.sleep(1)

    response = Response(stream_with_context(
        simulate_data_stream()), mimetype="text/event-stream")
    response.headers['Cache-Control'] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response
