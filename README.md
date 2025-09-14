Campus Chatbot 🤖
A multilingual conversational assistant designed to provide students with instant, round-the-clock information on campus queries. Built as a solution for the university hackathon, this chatbot helps streamline communication by deflecting routine inquiries and freeing up staff for more complex tasks.

<br>

<br>

Features ✨
Multilingual Support: Recognizes and responds to queries in English, Hindi, and Marathi.

Hybrid AI Model: Uses a pre-trained LLaMA model from Ollama for general conversations, supplemented by a Supabase database for accurate, institution-specific FAQs.

User-friendly Interface: A clean, responsive frontend built with HTML, CSS, and JavaScript.

Scalable Backend: A Python backend using the Flask framework to handle API requests and business logic.

Interaction Logging: All conversations are logged to Supabase for continuous improvement and analysis.


<br>

<br>

Technologies Used 💻
Frontend: HTML, CSS, JavaScript

Backend: Python, Flask

LLM: Ollama (locally-run LLaMA 3.1)

Database: Supabase (free tier)

<br>

<br>

Project Structure 📂
The repository is organized into a clear and logical structure:

chatbot-project/
├── frontend/
│ ├── index.html         # Main chatbot interface
│ ├── style.css          # Styling for a beautiful UI
│ └── script.js          # Handles client-side logic
├── backend/
│ ├── main.py            # Flask application logic
│ ├── requirements.txt   # Python dependencies
│ ├── .env               # Environment variables (private)
│ └── seed_db.py         # Script to ingest FAQ data into Supabase
└── data/
    └── faqs.csv         # Institutional FAQ data
<br>

<br>

Setup and Installation 🚀
Follow these steps to get the project up and running on your local machine.

1. Prerequisites
Python 3.8+

Git

Ollama (download and install)

2. Clone the Repository
Bash

git clone https://github.com/nandini-glitch/campus-chatbot.git
cd campus-chatbot
3. Backend Setup
Navigate to the backend directory.

Bash

cd backend
Create a virtual environment and install the required packages.

Bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Create a .env file in the backend directory with your Supabase credentials.

SUPABASE_URL="YOUR_SUPABASE_URL"
SUPABASE_KEY="YOUR_SUPABASE_KEY"
4. Database Seeding
First, create the faqs table in your Supabase project with the schema: question_en, question_hi, question_mr, answer_en, answer_hi, answer_mr.
Then, run the seed_db.py script to upload your FAQ data.

Bash

python seed_db.py
5. Run the Chatbot Locally
Step A: Start Ollama
Open a new terminal and run the Ollama server.

Bash

ollama serve
Step B: Pull the LLM
In a separate terminal, pull the required multilingual model.

Bash

ollama pull llama3.1
Step C: Start the Backend
In your backend terminal, run the Flask application.

Bash

python main.py
Step D: Open the Frontend
Open the frontend/index.html file in your web browser. The chatbot should now be operational.

<br>

<br>

We welcome suggestions for improvements.

Future enhancements could include:

Adding support for more regional languages.

Implementing a more sophisticated language detection model.

Building a dashboard for visualizing conversation logs. 

PDF Parsing, Additional Language Support, Full FAQ Coverage.
