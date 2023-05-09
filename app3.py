import hmac
import hashlib
import json
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

def verify_signature(request, secret):
    signature_header = request.headers.get('X-Square-Signature')
    if not signature_header:
        return False

    body = request.get_data()
    key = bytes(secret, 'utf-8')
    digest = hmac.new(key, body, hashlib.sha1).hexdigest()

    return hmac.compare_digest(digest, signature_header)

def write_log(event):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_data = f"{timestamp} - Received event: {json.dumps(event)}\n"
    
    with open('webhook_logs.txt', 'a') as log_file:
        log_file.write(log_data)

@app.route('/webhook', methods=['POST'])
def webhook():
    square_secret = 'your-square-webhook-signature-key'
    if not verify_signature(request, square_secret):
        return jsonify(success=False, error="Invalid signature"), 400

    event = request.get_json()
    
    print("Received event:", event)
    write_log(event)  # Write the log of the incoming webhook to a file
    
    # Process the event here (e.g., update database, send notifications, etc.)
    
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(port=3000)
