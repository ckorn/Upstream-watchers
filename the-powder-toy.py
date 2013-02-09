#!/usr/bin/python
import re
import urllib2
import sys
h=urllib2.urlopen("http://powdertoy.co.uk/Download.html").read()
v_finder=re.compile('Version (?P<version>[\d\.]+) for (?:.*)</div>', re.M)
m=v_finder.finditer(h)
if not m: sys.exit()
for x in m:
	v=x.group("version")
	print "<a href='https://github.com/FacialTurd/The-Powder-Toy/tags/%s'>%s</a>"%(v,v)
