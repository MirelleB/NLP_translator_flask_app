from flask import Flask, request, render_template
import socket


# instanciate Flask
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hostname = socket.gethostname()
    if request.method == "GET":
        return render_template("index.html", hostname = hostname)

    input = request.get_data().decode('UTF-8')
    translated_text =  'Load'
    return {'translated_text': translated_text}
