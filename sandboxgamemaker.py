#!/usr/bin/python
import urllib2
import re
h=urllib2.urlopen("http://www.sandboxgamemaker.com/free-game-maker-downloads").read()
f=re.compile("Platinum Arts Sandbox Free 3D Game Maker (?P<version>[\d\.]+)")
m=f.finditer(h)
for x in m:
	v = x.group("version")
	print "<a href='http://www.sandboxgamemaker.com/%s'>%s</a>"%(v,v)
