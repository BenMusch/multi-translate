# -*- coding: utf-8 -*-
import json
import os
import pprint

from chalice import Chalice
from google.cloud import translate
from google.oauth2 import service_account

app = Chalice(app_name='multi-translate')
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


@app.route('/')
def index():
    return client.get_languages()


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
