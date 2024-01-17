<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Dashboard</title>
</head>

<body>
    
<?php
include 'master.php';
?>

<div class="content">
  <button type="submit" id="Refresh" onclick="login()">Refresh</button>
  <iframe width="1280" height="720" src="http://localhost/Reports/powerbi/rajdashboardtest1?rs:embed=true" frameborder="0" style="border:0" allowfullscreen></iframe>
</div>

</body>
</html>