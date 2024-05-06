from flask import Flask, request
from nlp_interpreter import process_prompt, classify_prompt, classify_multiple_prompt
app = Flask(__name__)

@app.route("/api/nlp/process")
def nlp_process():
    data = request.args.get('data')
    json_schema = '''{  "type": "object",  "properties": {    "name": {      "type": "string"  },    "emotion": {      "type": "string"    }  },  "required": [    "name",    "emotion"  ]}'''
    return process_prompt(data, model_name = "llama3", json_schema = json_schema)

@app.route("/api/nlp/classify")
def nlp_classify():
    data = request.args.get('data')
    options = ["create", "delete", "edit"]
    return classify_prompt(data, model_name = "llama3", options = options)

@app.route("/api/nlp/classify_into_multiple")
def nlp_classify_into_multiple():
    data = request.args.get('data')
    options = ["create", "delete", "edit"]
    return classify_multiple_prompt(data, model_name = "llama3", options = options)

if __name__ == "__main__":
    app.run(debug=True)