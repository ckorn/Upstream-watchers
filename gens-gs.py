#!/usr/bin/python
import urllib2
import urllib
import re
import sys
import subprocess
import shlex

DOMAIN="http://segaretro.org"
URL="%s/Gens/GS"%(DOMAIN)
try:
	r=urllib2.urlopen(URL)
	html=r.read()
except urllib2.HTTPError, e:
	html=e.read()

# This odd DDOS filter seems to be disabled again
print html
sys.exit()

jschl_vc_finder = re.compile('(?:.*)<input type="hidden" name="jschl_vc" value="(?P<value>[^"]+)"/>(?:.*)', re.DOTALL)
m=jschl_vc_finder.match(html)
if not m: sys.exit()

jschl_vc=m.group("value")
#print jschl_vc

jschl_answer_finder = re.compile("(?:.*)\$\('#jschl_answer'\).val\((?P<value>[^)]+)\);(?:.*)", re.DOTALL)
m=jschl_answer_finder.match(html)
if not m: sys.exit()

jschl_answer=m.group("value")
#print jschl_answer

jschl_answer=eval("str(int(%s))"%(jschl_answer))
#print jschl_answer

formdata = { "act" : "jschl", "jschl_vc": jschl_vc, "jschl_answer" : jschl_answer }
#print formdata
data_encoded = urllib.urlencode(formdata)

# It is not working with urllib2
command="/usr/bin/wget -O- %s --post-data '%s'"%(URL,data_encoded)
#command="/usr/bin/curl %s -d '%s' -D-"%(URL,data_encoded)
args = shlex.split(command)
html = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]

url_finder = re.compile('(?:.*)href="(?P<URL>[a-zA-Z0-9/]+Gens-gs-r(?:[\d]+)\.tar\.gz)"(?:.*)', re.DOTALL)
m=url_finder.match(html)
if not m: sys.exit()

url="%s%s"%(DOMAIN,m.group("URL"))
print "<a href='%s'>%s</a>"%(url,url)

"""
print "curl %s -d '%s' -D-"%(URL,data_encoded)
print "wget -O- %s --post-data '%s' | grep Source"%(URL,data_encoded)
try:
	txheaders={'User-agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}

	req=urllib2.Request(URL,data_encoded,txheaders)
	r=urllib2.urlopen(req)
	html=r.read()
except urllib2.HTTPError, e:
	print e.info()
	html=e.read()
"""
