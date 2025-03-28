import requests
import time
from twilio.rest import Client

# Substitua pelos seus valores do RD Station
RD_API_URL = "https://api.rd.services/platform"
RD_ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL2FwaS5yZC5zZXJ2aWNlcyIsInN1YiI6InhaR2o0dVpuc3d6Mk9pQjJQanV1SFVkR1JMNW5oU0FDNVFDLVM3bWg4ZmtAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vYXBwLnJkc3RhdGlvbi5jb20uYnIvYXBpL3YyLyIsImFwcF9uYW1lIjoiYXRvbWEiLCJleHAiOjE3MjI2MTI1NTgsImlhdCI6MTcyMjUyNjE1OCwic2NvcGUiOiIifQ.IUTPv2-AW8wbcjTGSkBGzrPh0rDN6I0hqBKHFm5iRMDT6JU0AKseEAAiealPxMiLXkIiIXuH7dJ6S4kXxuLqFNniktYm5SpynGhCmbZIyD1ByhyZNid7YCNhy6TgbGd1BiIg_XdYN8JizAsFaX_tG0KsIMzGFb4SSqvr0cXSwu0K4XeBz3GSI6FUnx8erfmOXd2q57b027IPmR2KPBFY4sKOEyKYZFnB5t_6IFyzXGzSCrT8qODlrW3uRJTsjJlANx3Eed7HIqFQFN2e8gGlXdZAmpeaL1rpGbOOG18DKhpFCyTE1rUV3L4j4OKwWVB5l00vEN6qYrcaKtO0VmNuJQ"

# Substitua pelos seus valores do Twilio
TWILIO_ACCOUNT_SID = 'ACba9e17742c9325a4ef2541731cc5f53b'
TWILIO_AUTH_TOKEN = '317c04f3f5483c7eb67fe5c727eabf0d'
TWILIO_PHONE_NUMBER = '+15015508348'  # Formato: 'whatsapp:+14155238886'

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def get_leads():
    url = f"{RD_API_URL}/workflows"
    headers = {
        "Authorization": f"Bearer {RD_ACCESS_TOKEN}"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Verifica se houve um erro HTTP
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return []

def send_whatsapp_message(phone_number, message):
    try:
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=f'whatsapp:+{phone_number}'
        )
        return message.sid
    except Exception as e:
        print(f"Error: {e}")
        return None

def automate_conversations():
    leads = get_leads()
    for lead in leads:
        phone_number = lead.get("personal_phone")
        if phone_number:
            message = f"Olá {lead.get('name')}, bem-vindo!"
            send_whatsapp_message(phone_number, message)

if __name__ == "__main__":
    while True:
        automate_conversations()
        time.sleep(3600)  # Executa a cada hora
