import urllib2 
import re
import locale
import request

headers = { 'User-Agent' :  'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:25.0) Gecko/20100101 Firefox/25.0'}
request = request.RequestUrl()
feeddata = request.open_url_and_get_content('http://hughes.sieve.com.br:8000/level1/', headers=headers)
pattern = r'R\$ ([\d\.,]+)'
match = re.search(pattern, feeddata)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
price = locale.atof(match.groups()[0])
print 'R$ %f' % price 
