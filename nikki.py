#!/usr/bin/python
import urllib2
import re
r=urllib2.urlopen("http://code.joyridelabs.de/nikki/src/CHANGELOG")
h=r.read()
finder=re.compile("^(?P<version>[\d\.]+)(?:.*)")
m=finder.match(h)
if m:
	v=m.group("version")
	print("<a href='http://joyridelabs.de/game/code/%s'>%s</a>"%(v,v))
