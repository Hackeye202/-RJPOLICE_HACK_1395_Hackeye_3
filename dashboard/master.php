<?php
session_start();

if (!isset($_SESSION["username"])) {
    header("location: login.php");
    exit();
}

$username = $_SESSION["username"];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="master.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,100..900;1,100..900&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
</head>

<body>

<div class="header">
    <button class="toggle-button" onclick="toggleSidebar()">☰</button>
    <h1 class="header-text">Dashboard</h1>
    <div class="img-container">
        <img src="images\RPLogo.png" alt="logo" class="logo">
        <img src="images\lion.png" alt="logo" class="logo">
    </div>
</div>

<div id="sidebar">
    <h3 id="Name">Welcome, <?php echo $username; ?>!</h3>
    <a href="dashboard.php" onclick="toggleSidebar()">Home</a>
    <a href="crime.php" onclick="toggleSidebar()">Crime</a>
    <a href="livefootage.php" onclick="toggleSidebar()">Live CCTV Footage</a>
    <a href="crimefootage.php" onclick="toggleSidebar()">Crime Footage</a>
    <a href="map.php" onclick="toggleSidebar()">Map</a>
    <a href="camera.php" onclick="toggleSidebar()">Cameras</a>
    <a href="alertmessage.php" onclick="toggleSidebar()">Alert Message</a>
    <a href="emergencynumbers.php" onclick="toggleSidebar()">Emergency Numbers</a>
    <a href="logout.php" id="logout-button" onclick="toggleSidebar()">Logout</a>
</div>

<script>
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const header = document.querySelector('.header');
    const content = document.querySelector('.content');

    if (sidebar.classList.contains('active')) {
        sidebar.classList.remove('active');
        sidebar.style.width = '0';
        header.style.marginLeft = '0';
        content.style.marginLeft = '0';
    } else {
        sidebar.classList.add('active');
        sidebar.style.width = '250px';
        header.style.marginLeft = '250px';
        content.style.marginLeft = '250px';
    }
}
</script>

</body>
</html>
