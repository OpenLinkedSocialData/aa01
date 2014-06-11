#! /usr/bin/env python
#-*- coding: utf8 -*-
# put this on /usr/local/bin/
# without .py extension
from twython import TwythonStreamer
import datetime, pymongo

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            now=datetime.datetime.now()
            nick=data['user']["screen_name"].encode('utf-8')
            shout=data['text'].encode('utf-8')
            shout_transaction={"time":now,"nick":nick,"shout":shout}
            try:
                client.aaserver.shouts.insert(shout_transaction)
            except:
                client=pymongo.MongoClient("mongodb://labmacambira:macambira00@ds031948.mongolab.com:31948/aaserver")
                client.aaserver.shouts.insert(shout_transaction)
            print shout_transaction

    def on_error(self, status_code, data):
        print status_code
print "iniciando streaming"
class tw4: # puxa 
    tak="iub8wm03f4sI4EMvxgdoicwIe"
    taks="wlMxqHGSKjrKjhTPhQtkdR9bUnK7sZyjgsUEEcxDlHqoJCHO4D"
    tat="18882547-183eFHigoFCYlZDh4IUSkVtsF6WM0CbX6yvu0Ah3a"
    tats="YrWWp3GNudB7rXgHaj6cokJyXM6SW3GUTmO1tqoIYv6Y9"
stream=MyStreamer(tw4.tak,tw4.taks,tw4.tat,tw4.tats)
stream.statuses.filter(track="#aao0")
