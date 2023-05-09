from datetime import date
from sqlalchemy import func
from models import User, Transaction
from config import SQUARE_WEBHOOK_SIGNATURE_KEY
import amano_utils
import email_utils

def extract_user_info(event):
    # Implement this function
    pass

def extract_transaction_amount(event):
    # Implement this function
    pass

def handle_webhook_event(event, db_session):
    # Extract user information and transaction amount from the webhook data
    user_info = extract_user_info(event)
    transaction_amount = extract_transaction_amount(event)

    # Store the user information and transaction amount in the database
    store_transaction(db_session, user_info, transaction_amount)
    
    # Calculate the user's total transaction amount for the day
    total_transaction_amount = get_total_transaction_amount_for_today(db_session, user_info)
    
    # If the total transaction amount for the day exceeds $20, issue a validation request
    if total_transaction_amount > 20:
        amano_utils.process_validation(user_info)

def store_transaction(db_session, user_info, transaction_amount):
    # Implement this function
    pass

def get_total_transaction_amount_for_today(db_session, user_info):
    # Implement this function
    pass
