#!/usr/bin/python
import re
import urllib2
import sys
h=urllib2.urlopen("http://www.xnview.com/en/xnviewmp/").read()
v_finder=re.compile('Download <strong>XnView MP (?P<version>[\d\.]+) :</strong>', re.M)
m=v_finder.finditer(h)
if not m: sys.exit()
for x in m:
	v=x.group("version")
	print "<a href='http://www.xnview.com/en/xnviewmp/%s'>%s</a>"%(v,v)
