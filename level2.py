import httplib
import urllib2 
import re
import locale

httplib.HTTPConnection.debuglevel = 1
request = urllib2.Request('http://hughes.sieve.com.br:8000/level2/')
opener = urllib2.build_opener()
request.add_header('User-Agent',
        'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:25.0) Gecko/20100101 Firefox/25.0')
request.add_header('Cookie', 'd53db4de415c4e858dc761595623a898=+; Path=/\r\n')
feeddata = opener.open(request).read()
pattern = r'R\$ ([\d\.,]+)'
match = re.search(pattern, feeddata)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
price = locale.atof(match.groups()[0])
print 'R$ %f' % price 
