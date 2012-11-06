#!/usr/bin/python
import httplib
for link in ["linux102"]:
	conn = httplib.HTTPConnection("www.warsow.net")
	conn.request("HEAD", "/download?dl=%s"%(link))
	res = conn.getresponse()
	print "<!-- %d %s -->"%(res.status, res.reason)
	h = res.getheaders()
	#print h
	for k,v in h:
		if k == "location":
			v = v.replace(".tar.gz", "_unified.tar.gz")
			print "<a href='%s'>%s</a>"%(v,v)
