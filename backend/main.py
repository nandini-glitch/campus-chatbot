import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client
import ollama
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/chat/*": {"origins": "http://127.0.0.1:5500"}})

# Supabase setup
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Function to get answer from Supabase
def get_answer_from_db(user_query, lang='en'):
    """
    Queries the Supabase database for a direct answer to the user's query.
    """
    try:
        query_column = f'question_{lang}'
        
        response = supabase.table("faqs").select(f'answer_{lang}').ilike(query_column, f'%{user_query}%').limit(1).execute()
        
        if response.data and len(response.data) > 0:
            return response.data[0][f'answer_{lang}']
        else:
            return None

    except Exception as e:
        print(f"Supabase query error: {e}")
        return "I'm sorry, I'm currently unable to retrieve information. Please try again later."

def get_ollama_response(user_query, chat_history):
    """
    Generates a response using the Ollama LLM.
    """
    try:
        response = ollama.chat(model='llama3.1', messages=[
            {'role': 'system', 'content': 'You are a helpful college information assistant. Respond in the same language as the user.'},
            *chat_history,
            {'role': 'user', 'content': user_query}
        ])
        return response['message']['content']
    except Exception as e:
        print(f"Ollama error: {e}")
        return "I'm sorry, I'm currently unable to process your request. Please try again later."

@app.route('/chat', methods=['POST'])
def chat():
    """
    Handles the chatbot's conversational flow.
    """
    data = request.json
    user_message = data.get("message", "")
    chat_history = data.get("history", [])
    
    # Get the language from the request body
    user_lang = data.get("language", "en") 

    # 1. Check the database for a direct answer using the selected language
    faq_response = get_answer_from_db(user_message, lang=user_lang)
    if faq_response:
        bot_response = faq_response
    else:
        # 2. If no direct match, use the LLM
        bot_response = get_ollama_response(user_message, chat_history)

    # 3. Log the interaction to Supabase
    try:
        supabase.table("conversations").insert({
            "user_message": user_message, 
            "bot_response": bot_response,
            "language": user_lang
        }).execute()
    except Exception as e:
        print(f"Supabase logging error: {e}")

    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)