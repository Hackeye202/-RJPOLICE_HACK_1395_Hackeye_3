<?php
session_start();

if ($_SESSION["role"] !== "admin") {
    http_response_code(403);
    die("<h1>403: Forbidden</h1>");    
}

$username = $_SESSION["username"];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="master.css">
</head>

<body>

<div class="header">
    <button class="toggle-button" onclick="toggleSidebar()">☰</button>
    <h1 class="header-text">Admin Dashboard</h1>
    <div class="img-container">
        <img src="images\RPLogo.png" alt="logo" class="logo">
        <img src="images\lion.png" alt="logo" class="logo">
    </div>
</div>

<div id="sidebar">
    <h3 id="Name">Welcome, <?php echo $username; ?>!</h3>
    <a href="admindashboard.php" onclick="toggleSidebar()">Home</a>
    <a href="viewfaces.php" onclick="toggleSidebar()">View Existing Faces</a>
    <a href="addofficer.php" onclick="toggleSidebar()">Add Officers</a>
    <a href="addface.php" onclick="toggleSidebar()">Add Faces</a>
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
