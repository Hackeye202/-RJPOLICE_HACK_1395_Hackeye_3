<?php
include 'masteradmin.php';
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Upload</title>
    <link rel="stylesheet" href="addface.css">
    <script type="module">
        import { initializeApp } from 'https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js'
        import { getStorage, ref, uploadBytes } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-storage.js"

        const firebaseConfig = {
            apiKey: "AIzaSyBAB4_9gwbFSNwthq2y73S3wOX2vm4TGmA",
            authDomain: "hackeye-hackathon.firebaseapp.com",
            projectId: "hackeye-hackathon",
            storageBucket: "hackeye-hackathon.appspot.com",
            messagingSenderId: "236146676628",
            appId: "1:236146676628:web:35d40ca22d14bc4a31b581",
            measurementId: "G-D767X1E983"
        };

        const app = initializeApp(firebaseConfig);
        const storage = getStorage();

        // Add an event listener to handle file selection
        document.addEventListener('DOMContentLoaded', function () {
            const fileInput = document.getElementById('fileInput');

            fileInput.addEventListener('change', (e) => {
                const file = e.target.files[0];

                // Create a reference to the storage bucket and the file
                const storageRef = ref(storage, 'criminals/' + file.name);

                // Upload the file
                uploadBytes(storageRef, file).then((snapshot) => {
                    console.log('File uploaded successfully!');
                }).catch((error) => {
                    console.error('Error uploading file:', error);
                });
            });
        });
    </script>
</head>
<body>
    <h2>Add Criminal Faces</h2>
    <form id="uploadForm" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post" enctype="multipart/form-data">
        <table id="image-table">
            <tr>
                <th>Index</th>
                <th>Image</th>
                <th>Preview</th>
                <th>Action</th>
            </tr>
            <tr class="image-input" data-index="0">
                <td>0</td>
                <td><input type="file" name="images[]" accept="image/*" id="fileInput" required></td>
                <td><img id="previewImage0" alt="Image Preview" style="max-width:100px; max-height:100px;"></td>
                <td><button type="button" onclick="removeImage(this)">Remove</button></td>
            </tr>
        </table>
        <button type="button" onclick="addImage()">Add Image</button>
        <!-- Removed the onclick attribute from the submit button -->
        <button type="submit" id="uploadButton">Upload Images</button>
    </form>

    <script src="script.js"></script>
</body>
</html>
