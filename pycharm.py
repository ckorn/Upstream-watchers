#!/usr/bin/python
import re
import urllib2
import json

def main():
	h=urllib2.urlopen("https://data.services.jetbrains.com/products/releases?code=PCP%2CPCC&latest=true&type=release").read()
	j=json.loads(h)
	#print json.dumps(j, indent=4, sort_keys=True)
	url=j["PCC"][0]["downloads"]["linux"]["link"]
	print "<a href='%(url)s'>%(url)s</a>"%locals()
	

if __name__ == "__main__":
	main()
