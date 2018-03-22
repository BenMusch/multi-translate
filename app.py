import logging

from chalice import Chalice

from chalicelib import translate


app = Chalice(app_name='multi-translate')
app.log.setLevel(logging.DEBUG)

@app.route("/")
def index():
    return translate.available_languages

@app.route("/translate", methods=["POST"], cors=app.debug)
def perform_translation():
    request_data = app.current_request.json_body
    result = translate.translate(request_data["text"], int(request_data["numTranslations"]))
    return result
