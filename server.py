from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    form_name = data.get('form_name')  # Assuming form name is sent in JSON
    
  
    return jsonify({'status': 'Form not processed'}), 400


@app.route('/test', methods=['GET'])
def test():
    # A simple endpoint to test if the server is running
    return jsonify({'message': 'Hello, World!'})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
