document.addEventListener("DOMContentLoaded", function () {
    const videoUrlInput = document.getElementById("videoUrl");
    const downloadButton = document.getElementById("downloadButton");
    const downloadStatus = document.getElementById("downloadStatus");

    downloadButton.addEventListener("click", function () {
        const videoUrl = videoUrlInput.value;
        if (!videoUrl) {
            downloadStatus.innerText = "Please enter a YouTube video URL.";
            return;
        }

        downloadStatus.innerText = "Downloading... Please wait.";

        fetch(`/download?videoUrl=${encodeURIComponent(videoUrl)}`)
            .then(response => response.text())
            .then(data => {
                downloadStatus.innerHTML = data;
            })
            .catch(error => {
                downloadStatus.innerText = `Error: ${error.message}`;
            });
    });
});
