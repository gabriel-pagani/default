document.addEventListener("DOMContentLoaded", function () {
  var myChart = echarts.init(document.getElementById("main"), null, {
    renderer: "svg",
  });

  var option = {
    xAxis: {
      data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    },
    yAxis: {},
    series: [
      {
        type: "bar",
        data: [23, 24, 18, 50, 27, 28, 50],
      },
    ],
  };

  myChart.setOption(option);
});
