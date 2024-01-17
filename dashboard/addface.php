<?php
include 'masteradmin.php';

$uploadDir = 'images/criminals/';
$uploadStatus = array();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!empty($_FILES['images']['name'])) {
        $uploadedFiles = $_FILES['images'];
        $names = $_POST['names'];

        $allowedExtensions = array('jpg', 'jpeg', 'png', 'gif');

        foreach ($uploadedFiles['name'] as $index => $fileName) {
            $subfolderName = $names[$index];
            $subfolderPath = $uploadDir . $subfolderName . '/';

            if (!file_exists($subfolderPath)) {
                mkdir($subfolderPath, 0777, true);
            }

            $imageFileType = strtolower(pathinfo($fileName, PATHINFO_EXTENSION));
            $uniqueFileName = $subfolderPath . $subfolderName . '_' . uniqid() . '.' . $imageFileType;

            while (file_exists($uniqueFileName)) {
                $uniqueFileName = $subfolderPath . $subfolderName . '_' . uniqid() . '.' . $imageFileType;
            }

            if (in_array($imageFileType, $allowedExtensions)) {
                if (move_uploaded_file($uploadedFiles['tmp_name'][$index], $uniqueFileName)) {
                    $uploadStatus[] = 'File ' . $fileName . ' is valid and was successfully uploaded to ' . $subfolderName . '.';
                } else {
                    $uploadStatus[] = 'Upload failed for file ' . $fileName . '.';
                }
            } else {
                $uploadStatus[] = 'Invalid file format for file ' . $fileName . '. Only JPG, JPEG, PNG, and GIF files are allowed.';
            }
        }

        foreach ($uploadStatus as $status) {
            echo $status . '<br>';
        }
    } else {
        echo 'No files uploaded.';
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Criminal Faces</title>
    <link rel="stylesheet" href="addface.css">
</head>
<body>
    <h2>Add Criminal Faces</h2>
    <form id="uploadForm" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post" enctype="multipart/form-data">
        <table id="image-table">
            <tr>
                <th>Index</th>
                <th>Name</th>
                <th>Image</th>
                <th>Preview</th>
                <th>Action</th>
            </tr>
            <tr class="image-input" data-index="0">
                <td>0</td>
                <td><input type="text" name="names[]" required></td>
                <td><input type="file" name="images[]" accept="image/*" onchange="previewImage(this)" required></td>
                <td><img id="previewImage0" alt="Image Preview" style="max-width:100px; max-height:100px;"></td>
                <td><button type="button" id="remove-button" onclick="removeImage(this)">Remove</button></td>
            </tr>
        </table>
        <button type="button" onclick="addImage()">Add Image</button>
        <button type="submit" id="uploadButton">Upload Images</button>
    </form>

    <script src="script.js"></script>
</body>
</html>
