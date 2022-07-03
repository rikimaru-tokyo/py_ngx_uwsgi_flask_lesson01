from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"hello":"world"}), 200

@app.route('/health_check')
def health():
    return jsonify({"status":"OK"}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')

