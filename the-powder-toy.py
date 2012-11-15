#!/usr/bin/python
import re
import urllib2
import sys
h=urllib2.urlopen("https://github.com/FacialTurd/PowderToypp/tags").read()
v_finder=re.compile('Version (?P<version>[\d\.]+) (?:.*)\(build (?P<build>[\d]+)\)', re.M)
m=v_finder.finditer(h)
if not m: sys.exit()
for x in m:
	v=x.group("version")
	print "<a href='https://github.com/FacialTurd/PowderToypp/tags/%s'>%s</a>"%(v,v)
