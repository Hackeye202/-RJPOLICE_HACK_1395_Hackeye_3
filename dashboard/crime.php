<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
    <title>Crime Info</title>
</head>

<body>

<?php
include 'master.php';
?>

<div class="content" style="display:flex;align-items: center;">
  <canvas id="myChart" style="width:100%;max-width:600px"></canvas>
  <canvas id="myChart1" style="width:100%;max-width:600px;margin-left: auto;"></canvas>
</div>

<script>
    const xValues = [100,200,300,400,500,600,700,800,900,1000];

new Chart("myChart", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [{ 
      data: [860,1140,1060,1060,1070,1110,1330,2210,7830,2478],
      borderColor: "red",
      fill: false,
      label:'Violence'
    }, { 
      data: [1600,1700,1700,1900,2000,2700,4000,5000,6000,7000],
      borderColor: "green",
      fill: false,
      label:'Theft',
    }, { 
      data: [300,700,2000,5000,6000,4000,2000,1000,200,100],
      borderColor: "blue",
      fill: false,
      label:'Fighting'
    }]
  },
  options: {
    legend: {display: true},
    title: {
      display: true,
      text: "Crime"
    }

  }
});

var x1Values = ["location1", "location2", "location3", "location4", "location5"];
var y1Values = [55, 49, 44, 24, 15];
var barColors = [
  "#b91d47",
  "#00aba9",
  "#2b5797",
  "#e8c3b9",
  "#1e7145"
];

new Chart("myChart1", {
  type: "doughnut",
  data: {
    labels: x1Values,
    datasets: [{
      backgroundColor: barColors,
      data: y1Values
    }]
  },
  options: {
    title: {
      display: true,
      text: "Crime Loacations"
    }
  }
});
</script>

</body>
</html>
