from flask import (
    Blueprint, Response, stream_with_context, render_template
)
from . import data_stream
import json
import time

detector = data_stream.AnomalyDetector()

bp = Blueprint("flaskr", __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/data')
def dump_data():
    def simulate_data_stream():
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
