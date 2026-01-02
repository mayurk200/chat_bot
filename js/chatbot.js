async function sendMessage() {
  const input = document.getElementById("userInput");
  const text = input.value.trim();
  if (!text) return;

  const chatBox = document.getElementById("chatBox");

  const userMsg = document.createElement("div");
  userMsg.className = "user";
  userMsg.innerText = text;
  chatBox.appendChild(userMsg);

  input.value = "";

  const botMsg = document.createElement("div");
  botMsg.className = "bot";
  botMsg.innerText = "Thinking...";
  chatBox.appendChild(botMsg);

  chatBox.scrollTop = chatBox.scrollHeight;

  try {
    const res = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ message: text })
    });

    const data = await res.json();
    botMsg.innerText = data.reply || "No response.";

  } catch {
    botMsg.innerText = "Backend not running.";
  }

  chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
  const input = document.getElementById("userInput");
  const text = input.value.trim();
  if (!text) return;

  const chatBox = document.getElementById("chatBox");

  // show user message
  const userMsg = document.createElement("div");
  userMsg.className = "user";
  userMsg.innerText = text;
  chatBox.appendChild(userMsg);

  input.value = "";

  // show bot placeholder
  const botMsg = document.createElement("div");
  botMsg.className = "bot";
  botMsg.innerText = "Thinking...";
  chatBox.appendChild(botMsg);

  try {
    const response = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message: text })
    });

    const data = await response.json();
    botMsg.innerText = data.reply;

  } catch (error) {
    botMsg.innerText = "Cannot connect to backend.";
  }

  chatBox.scrollTop = chatBox.scrollHeight;
}

