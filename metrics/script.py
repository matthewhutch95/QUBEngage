import subprocess

import requests


def run_tests():
    result = subprocess.run(["pytest", "-W", "ignore", "-s", "test_app.py"], capture_output=True, text=True)
    if result.returncode != 0:
        failure_message = result.stdout + result.stderr
        send_telegram_message(f"Tests failed! Details:\n{failure_message}")
    else:
        success_message = result.stdout
        send_telegram_message(success_message)


def send_telegram_message(message):
    bot_token = "6730100130:AAFOCE7sfuvH9jB5mfK_X72bo2VXhK34Pnw"
    chat_id = "6322510070"
    api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    response = requests.post(api_url, data=data)
    if response.status_code == 200:
        print("Message sent.")
    else:
        print(f"Failed. Status code: {response.status_code}")
    print(response.json())
