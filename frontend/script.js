document.getElementById('send-btn').addEventListener('click', sendMessage);
document.getElementById('user-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

const chatWindow = document.getElementById('chat-window');

function sendMessage() {
    const userInput = document.getElementById('user-input');
    const userMessage = userInput.value.trim();
    if (userMessage === '') return;

    // Get the selected language from the dropdown
    const languageSelect = document.getElementById('language-select');
    const selectedLang = languageSelect.value;

    appendMessage(userMessage, 'user');
    userInput.value = '';

    // Get chat history for context management
    const chatHistory = Array.from(chatWindow.children).map(msgDiv => {
        return {
            role: msgDiv.classList.contains('user') ? 'user' : 'bot',
            content: msgDiv.textContent.trim()
        };
    });

    // Send the message, chat history, and selected language to the backend
    fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            message: userMessage,
            history: chatHistory,
            language: selectedLang // Pass the selected language
        })
    })
    .then(response => response.json())
    .then(data => {
        appendMessage(data.response, 'bot');
    })
    .catch(error => console.error('Error:', error));
}

function appendMessage(message, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);
    messageDiv.textContent = message;
    chatWindow.appendChild(messageDiv);
    // Scroll to the bottom of the chat window
    chatWindow.scrollTop = chatWindow.scrollHeight;
}