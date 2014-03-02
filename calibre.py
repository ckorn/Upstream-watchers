#!/usr/bin/python
import httplib

def main():
	conn = httplib.HTTPConnection("status.calibre-ebook.com")
	conn.request("HEAD", "http://status.calibre-ebook.com/dist/src")
	res = conn.getresponse()
	print "<!-- %d %s -->"%(res.status, res.reason)
	h = res.getheaders()
	for k,v in h:
		if k == "location":
			print "<a href='%(v)s'>%(v)s</a>"%locals()

if __name__ == "__main__":
	main()
