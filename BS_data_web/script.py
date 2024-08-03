import requests # To make the API call request
import pandas as pd # To handle the data
from datetime import datetime # For date time manipulatioin
import os # For interaction with the system's OS
import sys
from cryptography.fernet import Fernet # For encrypting / decrypting variables
from dotenv import load_dotenv # For generating and writing to an .env file

# Load the .env file
load_dotenv()

# Function to decrypt environment variables
def decrypt_variable(encrypted_value, key):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_value.encode()).decode()

# Get the encryption key
encryption_key = os.getenv('ENCRYPTION_KEY').encode()

# Decrypt sensitive variables
# Based on you API's documentation, you might need more or less variables here
API_CODE = decrypt_variable(os.getenv('ENCRYPTED_API_CODE'), encryption_key)
API_USER = decrypt_variable(os.getenv('ENCRYPTED_API_USER'), encryption_key)
API_PASSWORD = decrypt_variable(os.getenv('ENCRYPTED_API_PASSWORD'), encryption_key)
api_endpoint = decrypt_variable(os.getenv('ENCRYPTED_API_ENDPOINT'), encryption_key)
data_endpoint = decrypt_variable(os.getenv('ENCRYPTED_DATA_ENDPOINT'), encryption_key)

# Function to get token from API
# For ouru case, this first call requests an API temporary token, to then be used to make the data request.
def get_token(api_endpoint):
    headers = {"Content-Type": "application/json"}
    data = {"Code": API_CODE, "User": API_USER, "Password": API_PASSWORD}
    response = requests.post(api_endpoint, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get('Token')
    else:
        raise Exception(f"Error receiving the token: {response.status_code}")

# Function to get data from API using the token
# The body of the request is specified by the API's documentation. Adjust those functions based on your API's specifications
def get_data(data_endpoint, token, departure_airport, arrival_airport, from_date):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    # The API's documentation requre this structure of the the API body's request
    body = {
        "DepartureAirport": departure_airport,
        "ArrivalAirport": arrival_airport,
        "FromDate": from_date
    }
    response = requests.post(data_endpoint, headers=headers, json=body)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}")

# Function to parse JSON response and convert it to a DataFrame
# In my project's case, I dont need all the data fetched form the endpoint. 
# Also I want to structure the data that I only need in a specific way, to export them as an .xlxs file later.
# So I am parsing the data based on my project's requirements
def parse_json_response(response_json, selected_date, departure_airport):
    parsed_data = []
    for item in response_json:
        check_in = item.get('CheckIn', '').split('T')[0]
        if check_in == selected_date:
            reservation_number = item.get('ReservationNumber', '')
            hotel_name = item.get('Hotel', {}).get('Name', '')
            room_name = item.get('Room', {}).get('Name', '')
            location_name = item.get('Location', {}).get('Name', '')
            leader_info = item.get('LeaderInfo', {})
            check_out = item.get('CheckOut', '').split('T')[0]
            pax_info = item.get('PaxInfo', [])
            flight_no = item.get('FlightNo', '')

            leader_full_name = f"{leader_info.get('Title', '')} {leader_info.get('Name', '')} {leader_info.get('Surname', '')}".strip()

            check_in_formatted = datetime.strptime(check_in, '%Y-%m-%d').strftime('%m/%d/%Y')
            check_out_formatted = datetime.strptime(check_out, '%Y-%m-%d').strftime('%m/%d/%Y')

            pax_info_adt = next((p['Count'] for p in pax_info if p['Type'] == 'ADT'), 0)
            pax_info_chd = next((p['Count'] for p in pax_info if p['Type'] == 'CHD'), 0)
            pax_info_inf = next((p['Count'] for p in pax_info if p['Type'] == 'INF'), 0)

            pax_count = f"{pax_info_adt} ADT, {pax_info_chd} CHD, {pax_info_inf} INF"

            # Appending the parsed data, the values on the left represent the column names that will be shown in the excel file.
            parsed_data.append({
                'VOUCHER NO': reservation_number,
                'HOTELNAME': hotel_name,
                'ROOM': room_name,
                'LOCATION': location_name,
                'NAME': leader_full_name,
                'CHECK IN': check_in_formatted,
                'CHECK OUT': check_out_formatted,
                'PAX COUNT': pax_count,
                'FLIGHT NO': flight_no,
                'DEPARTURE AIRPORT': departure_airport  
            })

    return pd.DataFrame(parsed_data)

# Main function to get token, fetch data, and save it to an Excel file
def main(arrival_airport, from_date, save_path):
    try:
        token = get_token(api_endpoint)
        all_data = []

        for departure_airport in ['value1', 'value2', 'valu3']:
            response_json = get_data(data_endpoint, token, departure_airport, arrival_airport, from_date)
            df_parsed = parse_json_response(response_json, from_date, departure_airport)
            all_data.append(df_parsed)

        final_df = pd.concat(all_data, ignore_index=True)
        final_df.to_excel(save_path, index=False)
        return f"Data successfully extracted to Excel file at: {save_path}"
    except Exception as e:
        return str(e)

# Entry point for the script
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <arrival_airport> <from_date> <save_path>")
        sys.exit(1)
    
    result = main(sys.argv[1], sys.argv[2], sys.argv[3])
    print(result)
