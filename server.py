from flask import Flask, request
from llm_classifier import classify_prompt, classify_multiple_prompt
from llm_processor import process_prompt

app = Flask(__name__)

@app.route("/api/nlp/process")
def nlp_process():
    data = request.args.get('data')
    return process_prompt(data)

@app.route("/api/nlp/classify")
def nlp_classify():
    data = request.args.get('data')
    return classify_prompt(data)

@app.route("/api/nlp/classify_into_multiple")
def nlp_classify_into_multiple():
    data = request.args.get('data')
    return classify_multiple_prompt(data)

if __name__ == "__main__":
    app.run(debug=True)