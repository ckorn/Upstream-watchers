#!/usr/bin/python
import urllib2
import re

r=urllib2.urlopen("http://jag.xlabsoft.com/download.php")
html=r.read()

finder=re.compile("(?:.*)<a href='(?:[^']+)'>(?P<version>jag-(?:[\d\.]+)-src\.(?:zip|xz|gz|bz2))</a>(?:.*)", re.DOTALL)
m=finder.match(html)
if m:
	v=m.group('version')
	print "<a href='%s'>%s</a>"%(v,v)
