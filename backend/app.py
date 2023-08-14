from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for the entire app

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data['expression']
    try:
        result = str(eval(expression))
        return jsonify({'result': result})
    except:
        return jsonify({'error': 'Invalid expression'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
