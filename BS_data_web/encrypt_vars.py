"""
Step-by-Step Breakdown
Import Required Modules

'os' for operating system interactions.
'Fernet' from cryptography.fernet for encryption and decryption.
'load_dotenv' and 'set_key' from dotenv to manage the .env file.
Load Existing .env File

Load environment variables from a .env file if it exists using load_dotenv().
Generate Encryption Key

Generate a new encryption key using Fernet.generate_key().
Create a Fernet cipher object for encryption and decryption using the generated key.
Store Encryption Key

Store the generated encryption key in the .env file using set_key().
This key will be used later to decrypt the encrypted variables.
Define Sensitive Variables

Define the sensitive information to be encrypted (e.g., API credentials and endpoints).
Encrypt Sensitive Variables

Encrypt each sensitive variable using the cipher.encrypt() method.
Convert the encrypted bytes to a string using .decode() for storage in the .env file.
Store Encrypted Variables

Store the encrypted variables in the .env file using set_key().
Completion Message

Print a message indicating that the sensitive variables have been successfully encrypted and stored.
Usage
Run encrypt_vars.py:

This script should be run once to encrypt and store the sensitive variables in the .env file.
Make sure the .env file is accessible and writable.
Environment Configuration:

After running this script, the .env file will contain both the encryption key and the encrypted variables.
The encryption key will be used in other scripts (e.g., script.py) to decrypt and use these variables securely.
Integration with Other Scripts:

In scripts that need to use these variables (like script.py), load the .env file, retrieve the encryption key, and decrypt the variables as needed.
By following this approach, sensitive information is protected, and the risk of exposure is minimized. 
Make sure to handle the .env file with care, ensuring it is not exposed or shared unintentionally.


"""




import os
from cryptography.fernet import Fernet # encryption / decryption library
from dotenv import load_dotenv, set_key

# Load the .env file
load_dotenv()

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher = Fernet(key)

# Store the key in .env file
set_key('.env', 'ENCRYPTION_KEY', key.decode())

# Define sensitive variables
# Based on your API's documentation those values may vary
API_CODE = 'yourAPIcode'
API_USER = 'yourAPIuser'
API_PASSWORD = 'yourAPIpassword'
API_ENDPOINT = 'https://api.your.api.endpoint.com/auth/v1/token' # e.g. endpoint for token request
DATA_ENDPOINT = 'https://api.your.api.endpoint.com/dispatch/v1/reports/List' # e.g. endpoint for data request

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
