
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "FB Auto Reply Bot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received webhook data:", data)
    # Logic to reply automatically would go here
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
