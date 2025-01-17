# app.py
from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Simulate a simple database
messages = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/send', methods=['POST'])
def send_message():
    # Get data from client
    data = request.get_json()
    message = data.get('message', '')
    
    # Server processing
    timestamp = datetime.now().strftime("%H:%M:%S")
    processed_message = {
        'text': message,
        'time': timestamp,
        'length': len(message)
    }
    
    # Store in "database"
    messages.append(processed_message)
    
    # Send response to client
    return jsonify({
        'status': 'success',
        'message': 'Server received your message!',
        'processed': processed_message
    })

@app.route('/api/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

@app.route('/api/clear', methods=['POST'])
def clear_messages():
    messages.clear()
    return jsonify({'status': 'success', 'message': 'All messages cleared'})

if __name__ == '__main__':
    app.run(debug=True)