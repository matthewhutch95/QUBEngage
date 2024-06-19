from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import script
from config import services

app = Flask(__name__)
CORS(app)


@app.route('/<path:target>')
def index(target):
    rancher_urls = services.get(target)
    if rancher_urls:
        parameters = request.args
        try:
            response = requests.get(rancher_urls, params=parameters)
            response.raise_for_status()
            if response.status_code == 200:
                json_content = response.json()
                return jsonify(json_content)
            else:
                return jsonify({'status': response.status_code, 'error': response.text})
        except requests.exceptions.RequestException as req_err:
            return f'Unable to connect: {str(req_err)}', 500
    else:
        return f'Error! No external service found for: {target}', 404


if __name__ == '__main__':
    script.run_tests()
