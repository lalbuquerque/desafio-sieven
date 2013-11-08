import httplib
import urllib2 
import re
import locale

httplib.HTTPConnection.debuglevel = 1
request = urllib2.Request('http://hughes.sieve.com.br:8000/level1/')
opener = urllib2.build_opener()
request.add_header('User-Agent',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0')
feeddata = opener.open(request).read()
pattern = r'R\$ ([\d\.,]+)'
match = re.search(pattern, feeddata)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
price = locale.atof(match.groups()[0])
print 'R$ %f' % price 
