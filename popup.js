document.getElementById("go").addEventListener("click", async () => {
    const input = document.getElementById("input").value;
    const outputEl = document.getElementById("output");

    try {
        const response = await fetch("http://127.0.0.1:8000/motivate",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({text: input})
            });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();
        outputEl.textContent = data.response;
    } catch (err) {
        outputEl.textContent = "Error connecting to AI engine. Make sure it's running.\n" + err;
    }

});
