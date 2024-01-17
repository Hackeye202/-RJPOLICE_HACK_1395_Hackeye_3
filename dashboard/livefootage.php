<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live Camera Feed</title>
    <style>
      h2 {
        color: #007BFF; 
        text-align: center;
        margin-bottom: 30px;
        font-size: 2em;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 2px;
        position: relative;
      }
    </style>
</head>

<body>

<?php
include 'master.php';
?>

<div class="content">
  <h2>Live Feed</h2>
  <video id="webcamFeed" width="100%" height="100%" allowfullscreen autoplay></video>

  <script>
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(function (stream) {
        var video = document.getElementById('webcamFeed');
        video.srcObject = stream;
      })
      .catch(function (err) {
        console.error('Error accessing webcam:', err);
      });
  </script>
</div>

</body>
</html>
