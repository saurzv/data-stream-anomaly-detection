$(document).ready(function () {
  // chart.js configureation
  const config = {
    data: {
      labels: [],
      datasets: [
        {
          label: "Random Dataset",
          borderColor: "#8DB38B",
          backgroundColor: "#04724D",
          pointRadius: 5,
          data: [],
          fill: false,
          type: "line",
        },
        {
          type: "scatter",
          label: "Anomalies",
          backgroundColor: "Red",
          data: [],
          fill: true,
          showLine: false,
          pointRadius: 10,
          options: {
            scales: {
              x: {
                type: "linear",
                position: "bottom",
              },
            },
          },
        },
      ],
    },
    options: {
      responsive: true,
      title: {
        display: true,
        text: "Efficient Data Stream Anomaly Detection",
      },
      // tooltips: {
      //   mode: "index",
      //   intersect: false,
      // },
      // hover: {
      //   mode: "nearest",
      //   // intersect: true,
      // },
      scales: {
        xAxes: [
          {
            display: true,
            scaleLabel: {
              display: true,
              labelString: "Data Key",
            },
          },
        ],
        yAxes: [
          {
            display: true,
            scaleLabel: {
              display: true,
              labelString: "Value",
            },
          },
        ],
      },
    },
  };

  const context = document.getElementById("canvas").getContext("2d");

  // make new chart
  const chart = new Chart(context, config);

  // source to listen on
  const source = new EventSource("/data");

  // on new message on source execute this function
  source.onmessage = function (event) {
    // parse json data
    const data = JSON.parse(event.data);

    var last_shifted_key = -1;

    // start shifting the graph after 30 data points
    if (config.data.labels.length === 30) {
      last_shifted_key = config.data.labels.shift();
      config.data.datasets[0].data.shift();

      // shift anomaly data when it reaches starting index
      if (last_shifted_key + 1 == config.data.datasets[1].data[0].x) {
        config.data.datasets[1].data.shift();
      }
    }

    // push new data
    config.data.labels.push(data.key);

    // if incoming data has length two => anomaly present (logic written in `main.py`)
    if (data.value.length == 2) {
      config.data.datasets[1].data.push({
        x: data.key,
        y: data.value[0],
      });
      config.data.datasets[0].data.push(data.value[0]);
    } else {
      config.data.datasets[0].data.push(data.value[0]);
    }

    // update chart with new data
    chart.update();
  };
});
