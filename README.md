# RDAUTOMACAOLEADS

Automação de leads integrando RD Station com envio de mensagens automáticas via WhatsApp e SMS, utilizando Twilio e PyWhatKit. Este projeto facilita o gerenciamento de leads, respondendo de forma automatizada através de webhooks.

## 🚀 Funcionalidades

- 📩 Envio automático de mensagens via WhatsApp (PyWhatKit).
- 📤 Envio de SMS utilizando Twilio.
- 🔄 Integração direta com RD Station através de Webhooks.
- 📊 Registro de interações com leads.

## 📂 Estrutura do Projeto

```
RD_AUTOMACAOLEADS/
│
├── app.py                   # Script principal para iniciar a aplicação
├── app_twilio.py            # Script para envio de SMS via Twilio
├── app_whatsappAPI.py       # Script para integração com WhatsApp
├── webhook.py               # Configuração do webhook de integração
├── webhook copy.py          # Backup do arquivo webhook.py
│
├── LICENSE                  # Licença do projeto
├── PyWhatKit_DB.txt         # Dependências para integração com WhatsApp
├── README.md                # Documentação do projeto
└── .gitattributes           # Configuração do Git
```

## ⚙️ Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/RD_AUTOMACAOLEADS.git
cd RD_AUTOMACAOLEADS
```

2. **Crie e ative um ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. **Instale as dependências:**
```bash
pip install -r PyWhatKit_DB.txt
```

4. **Configure as variáveis de ambiente:**
- Configure as credenciais do Twilio.
- Configure os tokens da API do RD Station.

## ▶️ Como Usar

- **Iniciar a aplicação principal:**
```bash
python app.py
```

- **Executar o envio de mensagens via WhatsApp:**
```bash
python app_whatsappAPI.py
```

- **Rodar o webhook:**
```bash
python webhook.py
```

## 📌 Dependências Principais

- [Twilio](https://www.twilio.com/)
- [PyWhatKit](https://pypi.org/project/pywhatkit/)
- [Flask](https://flask.palletsprojects.com/)

## 📄 Licença

Este projeto está licenciado sob a licença MIT.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📬 Contato

- 💼 [LinkedIn](https://linkedin.com/in/williamsousa-dev/)
- 💻 [GitHub](https://github.com/wilk2308)
- ✉️ E-mail: william.sousa@wfitech.com.br

