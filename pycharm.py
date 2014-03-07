#!/usr/bin/python
import re
import urllib2

def main():
	h=urllib2.urlopen("http://www.jetbrains.com/js2/version.js").read()
	v_finder=re.compile('var versionPyCharmLong = "(?P<version>[\d\.]+)";', re.M)
	m=v_finder.finditer(h)
	if not m: return
	for x in m:
		v=x.group("version")
		print "<a href='http://download-ln.jetbrains.com/python/pycharm-community-%(v)s.tar.gz'>%(v)s</a>"%locals()

if __name__ == "__main__":
	main()
