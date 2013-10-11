#!/usr/bin/python
import urllib2
import re
r=urllib2.urlopen("http://code.google.com/p/codeslayer/source/browse/")
h=r.read().split("\n")
finder=re.compile('(?:.*)<option value="(?P<version>.*)" >(?:.*)</option>(?:.*)')
for x in h:
	m=finder.match(x)
	if m:
		v=m.group("version")
		print("<a href='http://code.google.com/p/codeslayer/source/browse/%s'>%s</a>"%(v,v))
