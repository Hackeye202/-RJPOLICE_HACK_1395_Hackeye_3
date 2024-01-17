<?php
include 'masteradmin.php';


$imageDir = 'images/criminals/';


if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['remove']) && isset($_POST['filename'])) {
        $filename = $_POST['filename'];
        $subdirectory = $_POST['subdirectory'];
        $filePath = $imageDir . $subdirectory . '/' . $filename;
        if (file_exists($filePath)) {
            unlink($filePath);
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .card-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
        }

        .card {
            width: 300px;
            height: 400px;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            background-color:  #ddd;
            margin: 20px;
            text-align: center;
        }

        .card h2 {
            color: #333;
        }

        .card p {
            color: #666;
        }
        .card img {
            width: 100%;
            height: 70%;
            object-fit: cover;
            border-radius: 4px;
            margin-bottom: 10px;
        }

        .remove-btn {
            background-color: #00ff00;
            color: #fff;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
        }
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
    <title>Existing Criminal Faces</title>
</head>
<body>
    <h2>Existing Faces</h2>
    <div class="card-container">
        <?php
        $subdirectories = glob($imageDir . '*', GLOB_ONLYDIR);
        foreach ($subdirectories as $subdirectory) {
            $files = scandir($subdirectory);
            $subdirName = basename($subdirectory);
            foreach ($files as $file) {
                if (in_array(pathinfo($file)['extension'], ['jpg', 'jpeg', 'png', 'gif'])) {
                    echo '<div class="card">';
                    echo '<img src="' . $imageDir . $subdirName . '/' . $file . '" alt="' . pathinfo($file)['filename'] . '">';
                    echo '<h2>NAME: ' . $subdirName . '</h2>';
                    echo '<p>Insert Crime Here</p>';
                    echo '<form method="post">';
                    echo '<input type="hidden" name="filename" value="' . $file . '">';
                    echo '<input type="hidden" name="subdirectory" value="' . $subdirName . '">';
                    echo '<button type="submit" class="remove-btn" name="remove">Remove</button>';
                    echo '</form>';
                    echo '</div>';
                }
            }
        }
        ?>
    </div>
</body>
</html>
