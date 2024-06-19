import json
from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

from config import services

app = Flask(__name__)
CORS(app)


@app.route('/healthcheck')
def health_check():
    return 'ok'


@app.route('/<path:path>', methods=['GET', 'POST'])
def proxy(path):
    rancher_urls = services.get(path)

    if rancher_urls:
        parameters = request.args
        data = None

        if request.method == 'POST':
            data = request.data

        try:
            if request.method == 'GET':
                response = requests.get(rancher_urls, params=parameters)
            elif request.method == 'POST':
                response = requests.post(rancher_urls, params=parameters, data=data)
            else:
                return f'Unsupported HTTP method: {request.method}', 405

            response.raise_for_status()

            json_content = response.json()
            return jsonify(json_content)
        except requests.exceptions.HTTPError as http_err:
            if http_err.response.status_code == 400:
                try:
                    json_content = http_err.response.json()
                    return jsonify(json_content)
                except json.JSONDecodeError:
                    return http_err.response.text
            else:
                return f'Unable to connect: {str(http_err)}'
    else:
        return f'Error! No external service found for: {path}', 404


if __name__ == '__main__':
    app.run(port=8095)