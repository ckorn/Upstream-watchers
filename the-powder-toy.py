#!/usr/bin/python
import re
import urllib2
import sys
h=urllib2.urlopen("http://powdertoy.co.uk/").read()
v_finder=re.compile('<p class="extra-links">(?P<version>[\d\.]+) ', re.M)
m=v_finder.finditer(h)
if not m: sys.exit()
for x in m:
	v=x.group("version")
	print "<a href='http://powdertoy.co.uk/%s'>%s</a>"%(v,v)
