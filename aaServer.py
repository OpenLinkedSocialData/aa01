import os, pymongo, datetime
from flask import Flask, request

app = Flask(__name__)

client=pymongo.MongoClient("mongodb://labmacambira:macambira00@ds031948.mongolab.com:31948/aaserver")

@app.route('/shout/')
def shout():
    """Chamado com ?nick=prestoppc&shout=aa bb cc: codando o desenhado."""
    print request.args
    print request.args.get("tkey","")
    nick=request.args.get("nick","")
    shout=request.args.get("shout","")
    now=datetime.datetime.now()
    print nick, shout, now
    client.aaserver.shouts.insert({"time":now,"nick":nick,"shout":shout})
    return 'Hello World!'

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
