from flask import Flask
from flask import send_file
import random

app = Flask(__name__)



 
@app.route("/song")

def song():
    return send_file('song.json')

@app.route("/all")

def index():
    return send_file('song.json')

@app.route("/")

def random():
    f = open('song.json') #Aprire il file json
    data = json.load(f) #caricare l'oggetto dentro data
    return print(data['song'][random.randrange(0,2)]) #estrarre una riga a caso dal vettore data
    
# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run()