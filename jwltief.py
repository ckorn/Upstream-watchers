#!/usr/bin/python
import urllib2
import re

r=urllib2.urlopen("http://games.aleva.com.br/jwltief/")
html=r.read()

finder=re.compile('(?:.*)<a href="(?:[^"]+)">Jwltief (?P<version>[\d\.]+) Linux \(Debian/Ubuntu\)</a>(?:.*)', re.DOTALL)
m=finder.match(html)
if m:
	v=m.group('version')
	print "<a href='http://games.aleva.com.br/jwltief/%s'>%s</a>"%(v,v)
