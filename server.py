from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Parse the incoming JSON data
    data = request.json
    
    # Log or process the data here
    print(data)
    
    # Respond to the webhook
    return jsonify({'status': 'success', 'data': data})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
