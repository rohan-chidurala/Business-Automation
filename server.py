from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['GET'])
def webhook():
    # Access query parameters
    data = request.args.to_dict()  # Convert ImmutableMultiDict to dict
    
    # Return the query parameters as JSON
    return jsonify({'status': 'Success', 'received_data': data}), 200

@app.route('/test', methods=['GET'])
def test():
    # A simple endpoint to test if the server is running
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
