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
<<<<<<< HEAD
    client=pymongo.MongoClient("mongodb://labmacambira:macambira00@ds031948.mongolab.com:31948/aaserver")
    shouts=client.aaserver.shouts.find({},{"_id":0})
    shouts=("<br />"*2).join([str(ss)[1:-1] for ss in shouts][::-1]).replace("u'","").replace("'","")
    print(shouts)
    return shouts
=======
    shouts = client.aaserver.shouts.find({}, {"_id": 0}).sort([(u'_id', -1), ])
    return render_template('minimum_client.html', shouts=shouts)

>>>>>>> 7524c9897f384f55f4febf9a85f25386b9798372

@app.route('/shout/')
def shout():
    """Chamado com ?nick=prestoppc&shout=aa bb cc: codando o desenhado."""
<<<<<<< HEAD
    print(request.args)
    print(request.args.get("tkey",""))
    nick=request.args.get("nick","")
    shout=request.args.get("shout","")
    now=datetime.datetime.now()
    print(nick, shout, now)
    client=pymongo.MongoClient("mongodb://labmacambira:macambira00@ds031948.mongolab.com:31948/aaserver")
    client.aaserver.shouts.insert({"time":now,"nick":nick,"shout":shout})
=======
    print request.args
    print request.args.get("tkey", "")
    nick = request.args.get("nick", "")
    shout = request.args.get("shout", "")
    now = datetime.datetime.now()
    print nick, shout, now
    client.aaserver.shouts.insert({"time": now, "nick": nick, "shout": shout})
>>>>>>> 7524c9897f384f55f4febf9a85f25386b9798372
    return 'Hello World!'


@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
