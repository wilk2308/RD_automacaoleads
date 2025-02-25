import requests
import time
import pywhatkit as kit
from datetime import datetime, timedelta

# Substitua pelos seus valores do RD Station
RD_API_URL = "https://api.rd.services/platform/v1"
RD_ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL2FwaS5yZC5zZXJ2aWNlcyIsInN1YiI6InhaR2o0dVpuc3d6Mk9pQjJQanV1SFVkR1JMNW5oU0FDNVFDLVM3bWg4ZmtAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vYXBwLnJkc3RhdGlvbi5jb20uYnIvYXBpL3YyLyIsImFwcF9uYW1lIjoiYXRvbWEiLCJleHAiOjE3MjI2MTI1NTgsImlhdCI6MTcyMjUyNjE1OCwic2NvcGUiOiIifQ.IUTPv2-AW8wbcjTGSkBGzrPh0rDN6I0hqBKHFm5iRMDT6JU0AKseEAAiealPxMiLXkIiIXuH7dJ6S4kXxuLqFNniktYm5SpynGhCmbZIyD1ByhyZNid7YCNhy6TgbGd1BiIg_XdYN8JizAsFaX_tG0KsIMzGFb4SSqvr0cXSwu0K4XeBz3GSI6FUnx8erfmOXd2q57b027IPmR2KPBFY4sKOEyKYZFnB5t_6IFyzXGzSCrT8qODlrW3uRJTsjJlANx3Eed7HIqFQFN2e8gGlXdZAmpeaL1rpGbOOG18DKhpFCyTE1rUV3L4j4OKwWVB5l00vEN6qYrcaKtO0VmNuJQ"

# Função para obter a lista de leads com informações básicas
def get_lead_ids():
    url = f"{RD_API_URL}/leads"
    headers = {
        "Authorization": f"Bearer {RD_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Verifica se houve um erro HTTP
        leads_data = response.json()
        return [lead["uuid"] for lead in leads_data.get("leads", [])]
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - {response.text}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return []

# Função para obter detalhes de um lead
def get_lead_details(lead_id):
    url = f"{RD_API_URL}/leads/{lead_id}"
    headers = {
        "Authorization": f"Bearer {RD_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Verifica se houve um erro HTTP
        lead_details = response.json()
        return lead_details
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - {response.text}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return {}

# Função para formatar o número de telefone
def formatar_telefone(telefone):
    telefone = ''.join(filter(str.isdigit, str(telefone)))
    if not telefone.startswith('55'):
        telefone = '55' + telefone
    return telefone

# Função para enviar mensagem de boas-vindas
def enviar_mensagem_boas_vindas(nome, telefone):
    telefone = formatar_telefone(telefone)
    mensagem = f"Olá {nome}, bem-vindo(a)!"
    hora_envio = (datetime.now() + timedelta(minutes=2)).hour
    minuto_envio = (datetime.now() + timedelta(minutes=2)).minute

    print(f"Enviando mensagem para {telefone} ({nome}) às {hora_envio}:{minuto_envio}: {mensagem}")

    try:
        kit.sendwhatmsg(f"+{telefone}", mensagem, hora_envio, minuto_envio, wait_time=20)
    except Warning as w:
        print(f"Warning: {w}")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

# Função principal para automatizar as conversas
def automate_conversations():
    lead_ids = get_lead_ids()
    for lead_id in lead_ids:
        lead_details = get_lead_details(lead_id)
        if lead_details:
            phone_number = lead_details.get("personal_phone")
            nome = lead_details.get("name")
            if phone_number and nome:
                enviar_mensagem_boas_vindas(nome, phone_number)
                time.sleep(30)  # Pausa de 30 segundos entre envios

if __name__ == "__main__":
    while True:
        automate_conversations()
        time.sleep(3600)  # Executa a cada hora
