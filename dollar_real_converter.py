import requests, json, smtplib, os
from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv()
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"

def get_exchange_rate():
    try:
        data = json.loads(requests.get(url).text)
        return data[0]["valor"]
    except (requests.exceptions.RequestException, json.decoder.JSONDecodeError):
        print("Error: No internet connection or Invalid JSON response")
        return None

def send_email(exchange_rate):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(os.getenv("EMAIL"), os.getenv("PASSWORD"))
        msg = MIMEText(f"The current exchange rate is: R${exchange_rate}")
        msg.add_header('Subject', 'Exchange Rate Update')
        msg.add_header('From', os.getenv("EMAIL"))
        msg.add_header('To', os.getenv("EMAIL"))
        server.sendmail(os.getenv("EMAIL"), os.getenv("EMAIL"), msg.as_string())
        server.quit()
    except (smtplib.SMTPConnectError, smtplib.SMTPAuthenticationError) as e:
        print(f"Error: {e}")

def check_exchange_rate():
    exchange_rate = get_exchange_rate()
    if exchange_rate is not None:
        send_email(exchange_rate)
    else:
        print("Skipping email send")

import schedule, time
schedule.every().hour.do(check_exchange_rate)
while True: schedule.run_pending();time.sleep(1)
