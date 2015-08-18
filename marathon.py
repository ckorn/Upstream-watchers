#!/usr/bin/python
import httplib

for game in ("marathon", "marathon2", "infinity"):
	conn = httplib.HTTPSConnection("alephone.lhowon.org")
	conn.request("HEAD", "/download/data.php?game=%s"%(game))
	res = conn.getresponse()
	print "<!-- %d %s -->"%(res.status, res.reason)
	h = res.getheaders()
	for k,v in h:
		if k == "location":
			print "<a href='%s'>%s</a><br/>\n"%(v,v)
