<?php
include 'master.php';
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body,
        html {
            margin: 0;
            padding: 0;
            height: 100%;
        }

        .content {
            padding: 0px;
            margin-left: 0;
            transition: margin-left 0.5s;
            height: 100%;
        }

        iframe {
            width: 100%;
            height: 100%;
            border: 0;
        }
    </style>
</head>

<body>
    <div class="content">
        <iframe src="map.html" title="Map Integration" frameborder="0"></iframe>
    </div>
</body>

</html>