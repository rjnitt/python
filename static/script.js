//document.addEventListener("DOMContentLoaded", function () {
//    const form = document.querySelector("form");
//    const resultDiv = document.querySelector(".result");
//
//    form.addEventListener("submit", function (e) {
//        e.preventDefault();
//        const userInput = document.getElementById("user_input").value;
//
//        fetch("/", {
//            method: "POST",
//            body: new URLSearchParams({ user_input: userInput }),
//            headers: {
//                "Content-Type": "application/x-www-form-urlencoded",
//            },
//        })
//            .then((response) => response.text())
//            .then((data) => {
//                resultDiv.innerHTML = `
//                    <h2>Result:</h2>
//                    <pre>${data}</pre>
//                `;
//            });
//    });
//});
//
//
//

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
