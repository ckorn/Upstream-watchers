#!/usr/bin/python
import urllib2
import re
h=urllib2.urlopen("http://legendsthegame.net/index.php?m=fileswap").read()
f=re.compile('title="Download (?:.*) Linux (?:.*) (?P<version>[\d\.]+)"', re.M)
m=f.finditer(h)
for x in m:
	v=x.group("version")
	print "<a href='http://legendsthegame.net/%s'>%s</a>"%(v,v)
