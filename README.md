# Python-Web-API-Communication
This project primarily utilizes Python to make API requests to a specified endpoint. The fetched data is then parsed into a specific format and extracted as an .xlsx file.

This repository includes a tutorial on how to use these files and details the structure of the program. Note that all data used in the code are example data, meaning that running the repository’s code as-is will not work.

The goal of this program is to construct an API request based on values submitted through an input form, in order to fetch data from an endpoint’s database.

In this project, I adhered to the specifications outlined in the company’s API documentation. The company specifies that the body of the request must follow a specific format. It is advisable to adjust your code based on your API’s documentation.




Project-Tree:

- loading.html:
    This HTML code creates a loading screen that appears while the main content of a webpage is being prepared. Upon page load, a full-screen overlay displays a logo, and a progress bar that animates over 7 seconds. During this period, a "Loading..." caption is shown. After the animation completes, the user is redirected to 'index.html'.
  
- index.html:
  This HTML code creates a login page. The page features a centered login container with a company logo, a header, and a password input field. The container appears with a fade-in animation, enhancing the user experience. The form inside the container allows users to enter their password and submit it via a button. The page has a visually appealing background gradient and a copyright notice at the bottom. The design ensures accessibility and responsiveness across different devices and screen sizes.
  
- login.php:
  This PHP and HTML code handles user login. When the user submits the login form, the PHP script checks if the entered password matches the predefined value ('0000'). If the password is correct, the user is redirected to 'main.html' and their session is marked as logged in. If the password is incorrect, an error message is displayed. The login page itself includes a centered container with a company logo, a header, and a password input field.
  
- main.html:
  This HTML code creates a reservation form. The form allows users to select an arrival airport and a departure date, which are then submitted to 'process.php' for further processing. The page features a logo, a title, and a form within a container that includes a fade-in animation. An information icon opens a popup window with detailed help and support instructions. The popup includes a close icon and a button for email support.
  
- process.php:
  This PHP script processes reservation form submissions. It first ensures the user is logged in, then validates the input data (arrival airport and departure date). If the input is valid, it generates a unique filename for the output file and determines the save path in the user's Documents folder. The script then executes a Python script with the input parameters to generate the file. If the Python script is successful and the file exists, the script sends the file to the user for download. If the input is invalid or an error occurs, appropriate error messages are displayed.
  
- script.py:
  This Python script processes reservation data by interacting with an API to fetch and parse data, then saving the results to an Excel file. It first decrypts the necessary API credentials and endpoint URLs from environment variables. The script defines functions for obtaining an authentication token, fetching data, and parsing the response JSON into a DataFrame. The main function handles the entire workflow and saves the parsed data to an Excel file.
  
- encrypt_vars.py:
  This script encrypts sensitive API credentials and stores them securely in a `.env` file. It uses the `cryptography` library to generate an encryption key, which is also saved in the `.env` file. The script then encrypts sensitive information such as API codes, user credentials, and endpoint URLs. The encrypted values are stored in the `.env` file, ensuring that the original sensitive data is protected. The script prints a confirmation message once the encryption and storage process is completed.
  
- .env:
  This `.env` file contains encrypted values for API credentials and endpoints, ensuring sensitive information is protected. The file includes an encryption key (`ENCRYPTION_KEY`) and encrypted values for the API code, user, password, and endpoints. These encrypted values are to be decrypted programmatically when needed to securely access the sensitive information.



# Project Requirements

- Python version 3.1.0 +
- Apache Local Server (Xampp was used for test purposes, and apache web server for the development project).
- (If apache web server is configured, php should be configured too).
- "requirements.txt" extracted into python (to include all necessary libraries).
- Php and Python configured to run on any IDE. e.g. Visual Studio Code.

  * For the configuration of the above, you should follow the necessary documentations for each service, to make sure everything is configured correctly.
  * In case difficulties are faced along the way, I can be contacted at: danielt1621@gmail.com
