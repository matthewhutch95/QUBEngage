from flask import Flask, request, jsonify
import uuid

from flask_cors import CORS

app = Flask(__name__)

storedData = {}
CORS(app)


@app.route('/save/', methods=['POST'])
def save_data():
    key = str(uuid.uuid4())
    values = request.args.to_dict()
    storedData[key] = values
    return jsonify({"key": key, "message": "Entry saved"})


@app.route('/retrieve/', methods=['GET'])
def retrieve_data():
    key = request.args.get('key')

    if key is not None:
        data = storedData.get(key)
        if data is not None:
            return jsonify(data)
        else:
            return jsonify({"error": "Key not found"}), 404
    else:
        return jsonify({"error": "Key parameter missing"}), 400


if __name__ == '__main__':
    app.run(port=8290)
