
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Route to serve the index.html page
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to handle chat messages from frontend
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']

    # Send user message to Rasa server
    rasa_response = send_message_to_rasa(user_message)

    return jsonify(rasa_response)

def send_message_to_rasa(message):
    # Replace with your Rasa server URL
    rasa_server_url = 'http://localhost:5005/webhooks/rest/webhook'

    try:
        response = requests.post(rasa_server_url, json={"message": message})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

if __name__ == '__main__':
    app.run(debug=True)
