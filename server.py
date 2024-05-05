from flask import Flask, request
from main import process, classify, classify_multiple

app = Flask(__name__)

@app.route("/api/nlp/process")
def nlp_process():
    data = request.args.get('data')
    return process(data)

@app.route("/api/nlp/classify")
def nlp_classify():
    data = request.args.get('data')
    return classify(data)

@app.route("/api/nlp/classify_into_multiple")
def nlp_classify_into_multiple():
    data = request.args.get('data')
    return classify_multiple(data)

if __name__ == "__main__":
    app.run(debug=True)