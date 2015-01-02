#!/usr/bin/python
import urllib2
import re
import sys
DIR_URL  = "http://main1.frostwire.com/frostwire/"

def printlink(spiFile, spiDirectory):
	print "<a href='%s'>%s</a>"%(spiDirectory+spiFile,spiFile)

def download(spiUrl):
        request = urllib2.Request(url=spiUrl)
        result = urllib2.urlopen(request, timeout=2)
        return result.read()

if __name__ == "__main__":
	data = download(DIR_URL)
	data = data.split("\n")
	href_re = re.compile('<a href="(?P<sub_dir>\d[\d\.]+/)">')
	dirs = []
	for line in data:
		search_result = re.search(href_re, line)
		if not search_result: continue
		sub_dir = search_result.group("sub_dir")
		dirs += [sub_dir]
	dirs = dirs[::-1]
	for dir in dirs:
		download_dir = DIR_URL+dir
		data = download(download_dir).split("\n")
		tarball_re = re.compile('<a href="(?P<file>frostwire(?:-|\_)([\d\.]+)\.(?:noarch|orig)\.tar\.(?:gz|bz2|xz))">')
		for line in data:
			search_result = re.search(tarball_re, line)
			if not search_result: continue
			file = search_result.group("file")
			printlink(file, download_dir)
