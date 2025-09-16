from flask import Flask
from flask import send_file
import random
import json
from markupsafe import escape

app = Flask(__name__)

@app.route("/song")
def song():
    return send_file('song.json')

@app.route("/rnd")
def rnd():
    f = open('song.json') #Aprire il file json
    data = json.load(f) #caricare l'oggetto dentro data
    return data['song'][random.randrange(0,9)] #estrarre una riga a caso dal vettore data

@app.route('/song/<artista>')
def cerca_artista(artista):
    f = open('song.json')
    data = json.load(f)
    for song in data['song']:
        if song['artista'] == artista:
            return song
if __name__ == "__main__":
    app.run()