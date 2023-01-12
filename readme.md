# Introduction
In this report, we present an automated Python code that checks the dollar conversion price to Brazilian Real and sends an email with the result on a hourly basis. The purpose of this code is to provide the user with real-time information about the exchange rate, allowing them to make informed decisions about buying dollars.

# Background
The code uses the `requests` library to make a GET request to the Central Bank of Brazil's API and retrieve the latest exchange rate. It then uses the `json` library to parse the response and extract the exchange rate.

The `send_email()` function uses the `smtplib` library to connect to an SMTP server (in this case, Gmail's) and send an email with the current exchange rate.

Finally, the `check_exchange_rate()` function is scheduled to run every hour using the schedule library, and will run continuously.

# Implementation
The code is implemented in Python and makes use of several libraries such as `requests`, `json`, `smtplib`, `email`, and `schedule`. The `requests` library is used to make GET requests to the Central Bank of Brazil's API and retrieve the latest exchange rate. The `json` library is used to parse the response and extract the exchange rate. The `smtplib` library is used to connect to an SMTP server (in this case, Gmail's) and send an email with the current exchange rate. The schedule library is used to `schedule` the `check_exchange_rate()` function to run every hour.

To ensure the security and privacy of sensitive information such as email and password, the code uses the `python-dotenv` package to store these variables in a `.env` file and load them into the script.

# How to run the script
1. Install the required libraries by running the command: `pip install -r requirements.txt`

2. Create a `.env` file in the same directory as the script and store your sensitive information (email and password) as key-value pairs. You can check an example at `.env.example`.

3. Run the script by using the command `python dollar_real_converter.py`.

4. Make sure that you have less secure apps enabled in your email account settings

# Conclusion
The presented code provides a useful tool for keeping track of the dollar-real exchange rate and making informed decisions about buying dollars. The code is well-structured and makes use of popular libraries to handle various tasks, making it easy to understand and modify. The use of the `python-dotenv` package also ensures that sensitive information is kept secure.