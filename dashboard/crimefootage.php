<?php
include 'master.php';

$dsn = 'mysql:host=localhost;dbname=hackeye';
$username = 'root';
$password = '1234';

try {
    $pdo = new PDO($dsn, $username, $password);
    // Set PDO to throw exceptions on error
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo 'Connection failed: ' . $e->getMessage();
    exit();
}

function getCrimeType($dateTime) {
    global $pdo;

    $query = "SELECT type_of_crime FROM crime WHERE date_time = :dateTime";
    $statement = $pdo->prepare($query);
    $statement->bindParam(':dateTime', $dateTime);
    $statement->execute();

    $result = $statement->fetch(PDO::FETCH_ASSOC);

    return $result ? $result['crime_type'] : 'Unknown';
}

function generateVideoDataArray($videoFiles) {
    $videos = [];

    foreach ($videoFiles as $videoFile) {
        $videoName = pathinfo($videoFile, PATHINFO_FILENAME);
        $thumbnail = 'videos/crimes/thumbnails/' . $videoName . '-thumbnail.jpg';
        $dateTime = DateTime::createFromFormat('Y-m-d_H-i-s', $videoName);

        if ($dateTime) {
            $videoDate = $dateTime->format('Y-m-d');
            $videoTime = $dateTime->format('h:i A');
            $crimeType = getCrimeType($dateTime->format('Y-m-d H:i:s'));
        } else {
            $videoDate = 'Unknown';
            $videoTime = 'Unknown';
            $crimeType = 'Unknown';
        }

        $videos[] = [
            'thumbnail' => $thumbnail,
            'name' => $videoName,
            'date' => $videoDate,
            'time' => $videoTime,
            'crimeType' => $crimeType,
            'url' => $videoFile,
        ];
    }

    return $videos;
}

$selectedDate = isset($_POST['search_date']) ? $_POST['search_date'] : null;

if (isset($_POST['reset'])) {
    $selectedDate = null;
}

$videoFiles = getVideoFiles($selectedDate);
$videos = generateVideoDataArray($videoFiles);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crime Videos</title>
    <link rel="stylesheet" href="crimefootage.css">
</head>

<body>

<div class="content">
    <div class="search-container">
        <form method="post" action="">
            <label for="search_date">Select Date:</label>
            <input type="date" id="search_date" name="search_date">
            <button type="submit" class="search-button">Search</button>
            <button type="submit" name="reset" class="reset-button">Reset</button>
        </form>
    </div>


<div id="video-container" class="video-container"></div>
<?php
    if (empty($videoFiles)) {
        echo '<p id="no-video">No videos available.</p>';
    }
?>
</div>

<script>
    const videos = <?php echo json_encode($videos); ?>;

    const videoContainer = document.getElementById('video-container');
    videos.forEach(video => {
        const card = document.createElement('div');
        card.className = 'video-card';

        const thumbnail = document.createElement('img');
        thumbnail.src = video.thumbnail;
        thumbnail.alt = 'Video Thumbnail';
        thumbnail.className = 'video-thumbnail';
        card.appendChild(thumbnail);

        const details = document.createElement('div');
        details.className = 'video-details';
        details.innerHTML = `
            <p><strong>Name:</strong> ${video.name}</p>
            <p><strong>Date:</strong> ${video.date}</p>
            <p><strong>Time:</strong> ${video.time}</p>
            <p><strong>Type of Crime:</strong> ${video.crimeType}</p>
        `;
        card.appendChild(details);

        const playButton = document.createElement('button');
        playButton.innerText = 'Play';
        playButton.className = 'play-button';
        playButton.addEventListener('click', () => playVideo(video.url, card));
        card.appendChild(playButton);

        videoContainer.appendChild(card);
    });

    function playVideo(videoUrl, card) {
    const playingVideo = card.querySelector('.video-player');
    if (playingVideo) {
        playingVideo.pause();
        playingVideo.currentTime = 0;
        hideVideoPlayer(playingVideo, card);
    }

    const videoPlayer = document.createElement('video');
    videoPlayer.src = videoUrl;
    videoPlayer.controls = true;
    videoPlayer.className = 'video-player';

    const exitButton = document.createElement('button');
    exitButton.innerText = 'Exit';
    exitButton.className = 'exit-button';
    exitButton.addEventListener('click', () => hideVideoPlayer(videoPlayer, card));

    card.appendChild(videoPlayer);
    card.appendChild(exitButton);

    const playButton = card.querySelector('.play-button');
    playButton.innerText = 'Exit';

    videoPlayer.style.display = 'block';
    exitButton.style.display = 'block';
    }

    function hideVideoPlayer(videoPlayer, card) {
    videoPlayer.pause();
    videoPlayer.currentTime = 0;
    const exitButton = card.querySelector('.exit-button');
    exitButton.style.display = 'none';
    videoPlayer.style.display = 'none';
    const playButton = card.querySelector('.play-button');
    playButton.innerText = 'Play';
    }
</script>

</body>
</html>
