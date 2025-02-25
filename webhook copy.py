from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import pywhatkit as kit

app = Flask(__name__)

# Conjunto para armazenar IDs dos leads para os quais a mensagem já foi enviada
enviados = set()

@app.route('/auth', methods=['POST'])
def receive_webhook():
    data = request.json
    if data:
        print(f"Dados recebidos: {data}")
        leads = data.get('leads', [])
        for lead in leads:
            lead_id = lead.get('id')
            name = lead.get('name')
            # Procurar telefone nos possíveis campos
            phone_number = lead.get('personal_phone') or lead.get('mobile_phone') or lead.get('phone')
            if phone_number and name and lead_id not in enviados:
                print(f"Processando lead: Nome - {name}, Telefone - {phone_number}")
                enviar_mensagem_boas_vindas(name, phone_number)
                enviados.add(lead_id)  # Adicionar o ID do lead ao conjunto
        return jsonify({'status': 'success'}), 200
    return jsonify({'status': 'failed'}), 400

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

if __name__ == '__main__':
    print("Iniciando o servidor Flask...")
    app.run(port=5000, debug=True)
    print("Servidor Flask iniciado e escutando na porta 5000...")
