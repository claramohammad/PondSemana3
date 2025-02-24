import os

SLACK_API_URL = "https://slack.com/api/chat.postMessage"
SLACK_TOKEN = os.getenv("SLACK_TOKEN", "FAKE-TOKEN")
SLACK_CHANNEL_ID = "C12345678"  # ID fictício

if SLACK_TOKEN == "FAKE-TOKEN":
    print("Aviso: Você está usando um token falso. Os testes não enviarão mensagens reais.")
