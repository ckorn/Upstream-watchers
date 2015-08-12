#!/usr/bin/python
import httplib
import re
import urllib2
d = urllib2.urlopen("http://www.warsow.net/download").read()
v_finder=re.compile('<option value="(?P<warsow>warsow([\d]+))">', re.M)
m=v_finder.finditer(d)
if not m: sys.exit()
for link in m:
	warsow=link.group("warsow")
	conn = httplib.HTTPSConnection("www.warsow.net")
	conn.request("HEAD", "/download?dl=%s"%(warsow))
	res = conn.getresponse()
	print "<!-- %d %s -->"%(res.status, res.reason)
	h = res.getheaders()
	#print h
	for k,v in h:
		if k == "location":
			v = v.replace(".tar.gz", "_unified.tar.gz")
			print "<a href='%s'>%s</a>"%(v,v)
