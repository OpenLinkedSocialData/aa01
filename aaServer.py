# -*- coding: utf8 -*-
import pymongo
import datetime
from flask import Flask, request, jsonify, render_template
#  adicione
#  import urllib
#  urllib.urlretrieve("http://0.0.0.0:5000/shout?nick=%s&shout=%s"%("nickEscolhido",urllib.quote("mensagem formatada com urllib.quote"))
#  em um app python para enviar um shout

app = Flask(__name__)
client = pymongo.MongoClient("mongodb://labmacambira:macambira00@ds031948.mongolab.com:31948/aaserver")

@app.route('/allJson/')
def allJson():
    shouts = client.aaserver.shouts.find({}, {"_id": 0})
    shouts = [ss for ss in shouts]
    return jsonify(shouts=shouts)

@app.route('/minimumClient/')
def minimumClient():
    shouts = client.aaserver.shouts.find({}, {"_id": 0}).sort([(u'_id', -1), ])
    return render_template('minimum_client.html', shouts=shouts)

@app.route('/shout/')
def shout():
    """Chamado com ?nick=prestoppc&shout=aa bb cc: codando o desenhado."""
    print(request.args)
    print(request.args.get("tkey",""))
    nick=request.args.get("nick","")
    shout=request.args.get("shout","")
    now=datetime.datetime.now()
    print(nick, shout, now)
    client.aaserver.shouts.insert({"time":now,"nick":nick,"shout":shout})
    return 'Hello World!'
    return 'Shout succeeded!'

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
