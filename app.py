import logging

from chalice import Chalice

import translate


app = Chalice(app_name='multi-translate')
app.log.setLevel(logging.DEBUG)

@app.route("/")
def index():
    return translate.available_languages

@app.route("/translate", methods=["POST"])
def perform_translation():
    request_data = app.current_request.json_body
    try:
        result = translate.translate(request_data["text"], 10)
        return result
    except Exception as e:
        app.log.error(e)
        return ""
