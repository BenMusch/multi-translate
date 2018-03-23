import logging
import os

from chalice import Chalice, CORSConfig

from chalicelib import translate

app = Chalice(app_name='multi-translate')
app.log.setLevel(logging.DEBUG)

cors_config = CORSConfig(allow_origin=os.environ['TRANSLATE_ORIGIN'])

@app.route("/", cors=cors_config)
def index():
    return translate.available_languages

@app.route("/translate", methods=["POST"], cors=cors_config)
def perform_translation():
    request_data = app.current_request.json_body
    result = translate.translate(request_data["text"], int(request_data["numTranslations"]))
    return result
