# Efficient Data Stream Anomaly Detection

## Project Description

This project aims to develop a Python script capable of detecting anomalies in a continuous data stream. The script simulates real-time sequences of floating-point numbers, representing various metrics such as financial transactions, system metrics, or sensor readings. The primary objective is to identify unusual patterns, such as exceptionally high values or deviations from the norm, which may indicate potential issues or anomalies.

## Project Highlights

- Real-time anomaly detection in continuous data streams.
- Utilizes NumPy for efficient data manipulation.
- Leverages scikit-learn's IsolationForest model for outlier detection.
- Employs Charts.js library for real-time data visualization.

## Dependencies

The project relies on the following dependencies:

- **NumPy**: A fundamental library for scientific computing in Python, providing efficient numerical operations and data structures.
- **Flask**: A lightweight web development framework for building web applications and APIs.
- **scikit-learn**: A comprehensive machine learning library in Python, offering a wide range of algorithms, including IsolationForest for outlier detection.
- **Charts.js**: A JavaScript library for creating interactive charts and visualizations. (_CDN included in index.html_)

## Project Structure

The project is structured as follows:

```txt
project root
├── README.md   : Project documentation file.
├── .env        : Has FLASK_APP variable, project won't work without it. Remove it from gitignore after cloning.
├── flaskr      : Main project directory.
│   ├── __init__.py     :  Initialization file for the Flask application.
│   ├── data_stream.py  : Module containing the AnomalyDetector class for data stream simulation and anomaly detection.
│   ├── main.py         : Main script handling routing, real-time data stream simulation.
│   ├── static
│   │   ├── script.js   : JavaScript code for real-time data visualization using Charts.js and anomaly detection updates.
│   │   └── styles.css  : CSS stylesheet for the web application.
│   └── templates
│       └── index.html  : Main HTML template for the web application.
└── requirements.txt    :  File listing the project's Python dependencies.
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/saurzv/data-stream-anomaly-detection
```

2. Change directory

```bash
cd data-stream-anomaly-detection
```

3. Make virtual environment

```bash
python3 -m venv venv
```

4. Activate the virtual env

```bash
source venv/bin/activate
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

6. Run the flask app

```bash
flask run
```

## Additional Notes

- The Flask application runs on the default port 5000, accessible at http://localhost:5000/.
- A folder named **_instance_** should be created to store the **_config.json_** file, which contains configuration settings for the application.
- The **_anomalies.log_** file records all detected anomalies and their corresponding anomaly scores.
