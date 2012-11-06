#!/usr/bin/python
import urllib2
import re

URL="http://bazaar.launchpad.net/~xintx-ua/wakeonplan/wakeonplan/files"
TARGET_URL="http://bazaar.launchpad.net/~xintx-ua/wakeonplan/wakeonplan/changes/%s"

if __name__ == "__main__":
	r=urllib2.urlopen(URL)
	html = r.read()

	rev_finder=re.compile("(?:.*)</span> \(revision (?P<rev>[\d]+)\)</span>(?:.*)", re.DOTALL)
	finding=rev_finder.match(html)
	if finding:
		url=TARGET_URL%(finding.group("rev"))
		print "<a href='%s'>%s</a>"%(url,url)
