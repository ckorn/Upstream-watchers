#!/usr/bin/python
import urllib2
import re

h=urllib2.urlopen('http://tide.olympe.in/main.htm').read()
f=re.compile("\[version (?P<version>[\d\.]+)", re.M)
m=f.finditer(h)
for x in m:
	v = x.group("version")
	print "<a href='http://tide.olympe.in/%s'>%s</a>"%(v,v)

