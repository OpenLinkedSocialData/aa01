#! /usr/bin/env python
#-*- coding: utf8 -*-
# use com:
# sudo cp aa.py /usr/local/bin/aa
# aí na linha de comando:
# $aa fazendo x pq y

# Configuration:
NICK="anonymous"

import sys, string, urllib
if len(sys.argv)==1:
    print("usage: aa this is a aa shout, for registering ongoing work")
else:
    shout=string.join(sys.argv[1:]," ")
    mirrors="http://aaserver.herokuapp.com/", "http://aa.daniloshiga.com/"
    aastring="shout?nick=%s&shout=%s"%(NICK,urllib.quote(shout))

    n_mirrors = len(mirrors)
    for i in range(n_mirrors):
        url = mirrors[i] + aastring
        # print 'trying ' + url
        req = urllib2.Request(url)
        try: 
            r = urllib2.urlopen(req)
        except urllib2.URLError as e:
            print("Warning: aa shout could not log at " + url + " (URLError)")
            print("Cannot reach this server, reason: ")
            print(e.reason)
        except urllib2.HTTPError as e:
            print("Warning: aa shout could not log at " + url + " (HTTPError)")
            print("Server returned error: ")
            print e.code()
            print e.read()
        else:
            print("shout logged")
            break

            # Debug
            #  r.read()
            #  if  r.find("Shout succeeded") || r.find("Hello World!")
            #      print("shout logged")
            #  else 
            #      print("ERROR: aa shout could not log at " + url)
            #      print("Server request " + url  + " returned:")
            #      print r.read()
            #      break
        if (i + 1 < n_mirrors):
            print("trying another mirror")
