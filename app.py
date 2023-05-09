from flask import Flask, request, jsonify
from database import Session
from square_utils import extract_user_info, extract_transaction_amount, handle_webhook_event

app = Flask(__name__)

@app.before_request
def create_session():
    if not hasattr(request, 'db_session'):
        request.db_session = Session()

@app.teardown_request
def close_session(exception=None):
    if hasattr(request, 'db_session'):
        request.db_session.close()

@app.route('/webhook', methods=['POST'])
def webhook():
    event = request.get_json()
    
    # Handle the webhook event
    handle_webhook_event(event, request.db_session)

    return jsonify(success=True)

if __name__ == '__main__':
    app.run()
