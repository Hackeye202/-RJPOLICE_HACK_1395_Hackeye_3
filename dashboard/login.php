<?php
session_start();

$servername = "localhost";
$username = "root";
$password = "1234";
$dbname = "hackeye";


try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
    die();
}

$error = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];
    $role = $_POST["role"];

    $tsql = "";
    $params = array($username);

    if ($role === "admin") {
        $tsql = "SELECT * FROM admininfo WHERE username = ?";
    } elseif ($role === "officer") {
        $tsql = "SELECT * FROM officerinfo WHERE username = ?";
    }

    try {
        $stmt = $conn->prepare($tsql);
        $stmt->execute($params);

        if ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
            if (password_verify($password, $row['password'])) {
                $_SESSION["username"] = $username;
                $_SESSION["role"] = $role;
                if ($role === "admin") {
                    header("location: admindashboard.php");
                } else {
                    header("location: dashboard.php");
                }
                exit();
            } else {
                $error = "Invalid username or password";
            }
        } else {
            $error = "Invalid username or password";
        }
    } catch (PDOException $e) {
        echo "Error: " . $e->getMessage();
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="login.css">
    <script>
        function showLoginForm(role) {
            var loginBox = document.getElementById("login-box");
            var formHtml = '';
            if (role === 'admin') {
                formHtml = `
                    <h2>Admin Login</h2>
                    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
                        <input type="text" id="username" name="username" placeholder="Admin Username" required>
                        <input type="password" id="password" name="password" placeholder="Admin Password" required>
                        <input type="hidden" name="role" value="admin">
                        <button type="submit" value="Submit">Login</button>
                    </form>`;
            } else if (role === 'officer') {
                formHtml = `
                    <h2>Officer Login</h2>
                    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
                        <input type="text" id="username" name="username" placeholder="Officer Username" required>
                        <input type="password" id="password" name="password" placeholder="Officer Password" required>
                        <input type="hidden" name="role" value="officer">
                        <button type="submit" value="Submit">Login</button>
                    </form>`;
            }
            formHtml += `
                <h5><a href="#" onclick="showRoleSelection()">←Back</a></h5>`;
            loginBox.innerHTML = formHtml;
        }

        function showRoleSelection() {
            var loginBox = document.getElementById("login-box");
            var roleSelectionHtml = `
                <h2>Login</h2>
                <button onclick="showLoginForm('admin')">Admin</button>
                <button onclick="showLoginForm('officer')">Officer</button>`;

            loginBox.innerHTML = roleSelectionHtml;
        }
    </script>
</head>
<body>
    <div id="header">
        <img src="images/RPLogo.png" alt="Rajasthan Police" height=60>
        <h2>AI-Based Surveillance Monitoring</h2>
    </div>
    <div id="login-box">
        <h2>Login</h2>
        <button onclick="showLoginForm('admin')">Admin</button>
        <button onclick="showLoginForm('officer')">Officer</button>
    </div>
</body>
</html>
