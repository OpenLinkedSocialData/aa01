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
    urllib.urlretrieve("http://aaserver.herokuapp.com/shout?nick=%s&shout=%s"%(NICK,urllib.quote(shout)))
    print "shout logged"

