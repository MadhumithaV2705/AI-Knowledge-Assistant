async function sendMessage() {
    let input = document.getElementById("input").value;

    let response = await fetch("/ask", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({question: input})
    });

    let data = await response.json();

    document.getElementById("chat").innerHTML += 
        `<p><b>You:</b> ${input}</p>
         <p><b>AI:</b> ${data.answer}</p>`;
}
