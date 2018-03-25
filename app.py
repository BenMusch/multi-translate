import logging
import os

from chalice import Chalice, CORSConfig, BadRequestError

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
    if "text" not in request_data or "numTranslations" not in request_data:
        raise BadRequestError("Missing necessary fields")
    elif not valid_number(request_data["numTranslations"]):
        raise BadRequestError("Translation count is not a valid integer")

    translation_count = int(request_data["numTranslations"])
    if translation_count <= 0 or translation_count >= 16:
        raise BadRequestError("Translation count must be between 1 and 16")

    result = translate.translate(request_data["text"], int(request_data["numTranslations"]))
    return result

def valid_number(num_str):
    try:
        int(num_str)
        return True
    except Exception:
        return False
