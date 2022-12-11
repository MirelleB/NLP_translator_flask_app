from flask import Flask, request, render_template
from transformers import pipeline
import socket

# load model
pipe = pipeline("translation", model="t5-small")

# instanciate Flask
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hostname = socket.gethostname()
    if request.method == "GET":
        return render_template("index.html", hostname = hostname)

    input = request.get_data().decode('UTF-8')
    translated_text =  pipe(input)[0]['translation_text']
    return {'translated_text': translated_text}

@app.route("/translate/<text>", methods=["GET", "POST"])
def translate(text):
    hostname = socket.gethostname()
    translated_text =  pipe(text)[0]['translation_text']

    if request.method == "GET":
        return {'Instance':hostname, "translated_text":translated_text}

if __name__ == '__main__':
    # start Flask
    app.run(debug=True)
