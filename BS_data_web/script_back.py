import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv, set_key

# Load the .env file
load_dotenv()

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher = Fernet(key)

# Store the key in .env file
set_key('.env', 'ENCRYPTION_KEY', key.decode())

# Define sensitive variables
API_CODE = 'rhodesto'
API_USER = 'apiuser'
API_PASSWORD = 'loop1meew2DI@fing'
API_ENDPOINT = 'https://api.blue-style.cz/auth/v1/token'
DATA_ENDPOINT = 'https://api.blue-style.cz/dispatch/v1/reports/labelList'

# Encrypt sensitive variables
encrypted_api_code = cipher.encrypt(API_CODE.encode()).decode()
encrypted_api_user = cipher.encrypt(API_USER.encode()).decode()
encrypted_api_password = cipher.encrypt(API_PASSWORD.encode()).decode()
encrypted_api_endpoint = cipher.encrypt(API_ENDPOINT.encode()).decode()
encrypted_data_endpoint = cipher.encrypt(DATA_ENDPOINT.encode()).decode()

# Store encrypted variables in .env file
set_key('.env', 'ENCRYPTED_API_CODE', encrypted_api_code)
set_key('.env', 'ENCRYPTED_API_USER', encrypted_api_user)
set_key('.env', 'ENCRYPTED_API_PASSWORD', encrypted_api_password)
set_key('.env', 'ENCRYPTED_API_ENDPOINT', encrypted_api_endpoint)
set_key('.env', 'ENCRYPTED_DATA_ENDPOINT', encrypted_data_endpoint)

print("Sensitive variables encrypted and stored in .env file.")


