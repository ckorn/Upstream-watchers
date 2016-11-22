#!/usr/bin/python
import urllib2
import re
h=urllib2.urlopen("http://shinjiru.me/home").read()
f=re.compile("ng-init=\"version='(?P<version>[\d\.]+)'\"", re.M)
m=f.finditer(h)
for x in m:
	v=x.group("version")
	print "<a href='https://github.com/Kazakuri/Shinjiru/%s'>%s</a>"%(v,v)
