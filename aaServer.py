#-*- coding: utf8 -*-
import os, pymongo, datetime, string
from flask import Flask, request
# dicione
### import urllib
### urllib.urlretrieve("http://0.0.0.0:5000/shout?nick=%s&shout=%s"%("nickEscolhido",urllib.quote("mensagem formatada com urllib.quote"))
# em um app python para enviar um shout

app = Flask(__name__)


@app.route('/minimumClient/')
def minimumClient():
    client=pymongo.MongoClient("mongodb://labmacambira:macambira00@ds031948.mongolab.com:31948/aaserver")
    shouts=client.aaserver.shouts.find({},{"_id":0})
    shouts=string.join([str(ss)[1:-1] for ss in shouts][::-1],"<br />"*2).replace("u'","").replace("'","")
    print shouts
    return shouts

@app.route('/shout/')
def shout():
    """Chamado com ?nick=prestoppc&shout=aa bb cc: codando o desenhado."""
    print request.args
    print request.args.get("tkey","")
    nick=request.args.get("nick","")
    shout=request.args.get("shout","")
    now=datetime.datetime.now()
    print nick, shout, now
    client=pymongo.MongoClient("mongodb://labmacambira:macambira00@ds031948.mongolab.com:31948/aaserver")
    client.aaserver.shouts.insert({"time":now,"nick":nick,"shout":shout})
    return 'Hello World!'

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
