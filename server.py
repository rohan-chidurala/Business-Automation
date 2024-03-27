from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST', 'GET', 'PUT', 'DELETE'])
def webhook():
    if request.method == 'POST':
        # Handle POST request
        data = request.get_json()
        print('POST request received:', data)
        return jsonify({'status': 'received', 'data': data})
    
    elif request.method in ['GET', 'PUT', 'DELETE']:
        # Handle GET, PUT, DELETE requests
        # For these methods, you might want to return something else or handle differently
        data = request.args  # For GET, data will be in the query string
        print(f'{request.method} request received:', data)
        return jsonify({'status': 'received', 'data': data})

    else:
        # Other HTTP methods not allowed
        return jsonify({'status': 'error', 'message': 'Method not allowed'}), 405


@app.route('/test', methods=['GET'])
def test():
    # A simple endpoint to test if the server is running
    return jsonify({'message': 'Hello, World!'})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
