<?php
include 'masteradmin.php';

$servername = "localhost";
$username = "root";
$password = "1234";
$dbname = "hackeye";

try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    try {
        $userDetails = $_POST['user_details'];

        foreach ($userDetails as $index => $user) {
            $username = $user['username'];
            $password = password_hash($user['password'], PASSWORD_DEFAULT);

            if (isset($_POST['remove_user'][$index]) && $_POST['remove_user'][$index] == 'on') {
                continue;
            }

            $stmt = $conn->prepare("INSERT INTO officerinfo (username, password) VALUES (:username, :password)");
            $stmt->bindParam(':username', $username);
            $stmt->bindParam(':password', $password);
            $stmt->execute();

            echo "User '$username' registered successfully.<br>";
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
    <title>Officer Registration</title>
    <link rel="stylesheet" href="addofficer.css">
</head>
<body>

<h2>Officer Registration</h2>
<form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
    <table id="user-table">
        <tr>
            <th>Username</th>
            <th>Password</th>
            <th>Action</th>
        </tr>
        <tr class="user-input">
            <td><input type="text" name="user_details[0][username]" required></td>
            <td><input type="password" name="user_details[0][password]" required></td>
            <td><button type="button" id="remove-button" onclick="removeUser(this)">Remove</button></td>
        </tr>
    </table>
    <button type="button" onclick="addUser()">Add User</button>
    <input type="submit" id="register-button" value="Register">
</form>

<script>
    function addUser() {
        var table = document.getElementById('user-table');
        var index = table.rows.length;

        var row = table.insertRow(-1);
        row.className = 'user-input';

        var usernameCell = row.insertCell(0);
        usernameCell.innerHTML = `<input type="text" name="user_details[${index}][username]" required>`;

        var passwordCell = row.insertCell(1);
        passwordCell.innerHTML = `<input type="password" name="user_details[${index}][password]" required>`;

        var actionCell = row.insertCell(2);
        actionCell.innerHTML = `<button type="button" id="remove-button" onclick="removeUser(this)">Remove</button>`;
    }

    function removeUser(button) {
        var row = button.parentNode.parentNode;
        row.parentNode.removeChild(row);
    }
</script>

</body>
</html>
