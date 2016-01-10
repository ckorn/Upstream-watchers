#!/usr/bin/python
import re
import urllib2
import json

def main():
	h=urllib2.urlopen("https://data.services.jetbrains.com/products/releases?code=PCP%2CPCC&latest=true&type=release").read()
	j=json.loads(h)
	#print json.dumps(j, indent=4, sort_keys=True)
	print j["PCC"][0]["downloads"]["linux"]["link"]
	

if __name__ == "__main__":
	main()
