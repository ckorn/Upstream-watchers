#!/usr/bin/python
import urllib2
import re
URL="http://automated-builds-secondlife-com.s3.amazonaws.com/hg/repo/integration_viewer-development/arch/Linux/quicklink.html"

if __name__ == "__main__":
	f=urllib2.urlopen(URL)
	html=f.read()
	url_finder=re.compile("(?:.*)URL=(?P<url>.*\.tar\.(?:bz2|xz|gz))(?:.*)", flags=re.DOTALL)

	result=url_finder.match(html)
	if result:
		g=result.group("url")
		print "<a href='%s'>%s</a>"%(g,g)
