from flask import Flask, request, jsonify
import json
from datetime import datetime
import os

app = Flask(__name__)
MESSAGES_FILE = 'messages.json'

# Initialize messages file if it doesn't exist
if not os.path.exists(MESSAGES_FILE):
    with open(MESSAGES_FILE, 'w') as f:
        json.dump([], f)

@app.route('/api/messages', methods=['POST'])
def store_message():
    print("DEBUG: Received POST request")  # Add this line
    try:
        data = request.get_json()
        print(f"DEBUG: Received data: {data}")  # Add this line
        message = {
            'name': data['name'],
            'email': data['email'],
            'message': data['message'],
            'date': datetime.utcnow().isoformat()
        }
        
        # Read existing messages
        with open(MESSAGES_FILE, 'r') as f:
            messages = json.load(f)
        
        # Add new message
        messages.append(message)
        
        # Write back to file
        with open(MESSAGES_FILE, 'w') as f:
            json.dump(messages, f, indent=2)
            
        return jsonify({'success': True}), 201
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/messages', methods=['GET'])
def get_messages():
    with open(MESSAGES_FILE, 'r') as f:
        messages = json.load(f)
    return jsonify(messages)

if __name__ == '__main__':
    app.run(port=5000, debug=True)


