<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        table {
    width: 80%;
    margin: 20px auto;
    border-collapse: collapse;
        }

        th {
            background-color: #9a5cff;
            padding: 10px;
            text-align: center;
            border: 1px solid #000000;
        }
        td {
            border: 1px solid #000000;
            background-color: rgb(250, 221, 159);
            padding: 10px;
            text-align: center;
        }

        tr#Authority{
            background-color: rgb(0, 49, 211);
        }
    </style>
    <title>Emergency Numbers</title>
</head>

<body>

<?php
include 'master.php';
?>

<div class="content">
    <h1>Rajasthan Emergency Numbers</h1>
    <table>
        <thead>
            <tr>
                <th>Service</th>
                <th>Emergency Number</th>
            </tr>
        </thead>
        <tbody>
            <tr id="Authority">
                <td>Authority1</td>
                <td>9988776655</td>
            </tr>
            <tr id="Authority">
                <td>Authority2</td>
                <td>9876543210</td>
            </tr>
            <tr>
                <td>Police</td>
                <td>100</td>
            </tr>
            <tr>
                <td>Ambulance</td>
                <td>108</td>
            </tr>
            <tr>
                <td>Fire</td>
                <td>101</td>
            </tr>
        </tbody>
    </table>
</div>

</body>
</html>
