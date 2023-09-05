document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const resultDiv = document.querySelector(".result");

    form.addEventListener("submit", function (e) {
        e.preventDefault();
        const userInput = document.getElementById("user_input").value;

        fetch("/", {
            method: "POST",
            body: new URLSearchParams({ user_input: userInput }),
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
        })
            .then((response) => response.text())
            .then((data) => {
                resultDiv.innerHTML = `
                    <h2>Result:</h2>
                    <pre>${data}</pre>
                `;
            });
    });
});
