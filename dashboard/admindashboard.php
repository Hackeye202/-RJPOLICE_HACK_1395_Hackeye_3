<?php
include 'masteradmin.php';
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Admin Dashboard</title>
  <link rel="stylesheet" href="admindashboard.css"> 
  <script src="https://kit.fontawesome.com/83bda00a3e.js" crossorigin="anonymous"></script>
</head>
<body>
  <div class="card-container">
    <a href="viewfaces.php" class="card">
      <div class="card-content">
        <i class="fa-solid fa-users-viewfinder fa-6x"></i>
        <h3>View Existing Faces</h3>
        <p>View existing criminals' faces in your server.</p>
      </div>
    </a>

    <a href="addofficer.php" class="card">
      <div class="card-content">
        <i class="fa-solid fa-people-roof fa-6x"></i>
        <h3>Add Officers</h3>
        <p>Add Officers to your database to register them.</p>
      </div>
    </a>

    <a href="addface.php" class="card">
      <div class="card-content">
        <i class="fas fa-image-portrait fa-6x"></i>
        <h3>Add Faces</h3>
        <p>Add Faces to your database for face recognition.</p>
      </div>
    </a>
  </div>
</body>
</html>
