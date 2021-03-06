import random
import os

from google.cloud import translate
from google.oauth2 import service_account


creds = {
  "type": os.environ["GOOGLE_PROJECT_TYPE"],
  "project_id": os.environ["GOOGLE_PROJECT_ID"],
  "private_key_id": os.environ["GOOGLE_PRIVATE_KEY_ID"],
  "private_key": os.environ["GOOGLE_PRIVATE_KEY"].decode('unicode_escape'),
  "client_email": os.environ["GOOGLE_CLIENT_EMAIL"],
  "client_id": os.environ["GOOGLE_CLIENT_ID"],
  "auth_uri": os.environ["GOOGLE_AUTH_URI"],
  "token_uri": os.environ["GOOGLE_TOKEN_URI"],
  "auth_provider_x509_cert_url": os.environ["GOOGLE_AUTH_PROVIDER_X509_CERT_URL"],
  "client_x509_certurl": os.environ["GOOGLE_CLIENT_X509_CERT_URL"]
}
credentials = service_account.Credentials.from_service_account_info(creds)
client = translate.Client(credentials=credentials)

available_languages = client.get_languages()


def translate(text, num_translations):
    language_chain = [
            {"language": { "code": "en", "name": "English" }, "text": text}
    ]
    for _ in range(num_translations):
        new_lang = get_random_language()
        language_chain.append({
            "language": { "code": new_lang["language"], "name": new_lang["name"] }
        })

    language_chain.append({"language": { "code": "en", "name": "English" }})

    for i in range(1, len(language_chain)):
        src_text = language_chain[i-1]["text"]
        src_lang = language_chain[i-1]["language"]["code"]
        dst_lang = language_chain[i]["language"]["code"]
        translation = client.translate(src_text, source_language=src_lang, target_language=dst_lang)
        language_chain[i]["text"] = translation["translatedText"]
    return language_chain

def get_random_language():
    choice = random.choice(available_languages)
    while choice["language"] == "en":
        choice = random.choice(available_languages)
    return choice
    return choice
