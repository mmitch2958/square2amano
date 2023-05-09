from config import AMI_CREDENTIALS
import email_utils

def get_jwt_token(credentials):
    # Implement this function
    pass

def create_validation(jwt_token, validation_data):
    # Implement this function
    pass

def prepare_validation_data(user_info):
    # Implement this function
    pass

def process_validation(user_info):
    jwt_token = get_jwt_token(AMI_CREDENTIALS)
    validation_data = prepare_validation_data(user_info)
    validation = create_validation(jwt_token, validation_data)
    
    # Send the user an email with the QR code
    qr_code = validation["qr_code_number"]
    email_utils.send_qr_code_email(user_info["email"], qr_code)
    
    # Store
