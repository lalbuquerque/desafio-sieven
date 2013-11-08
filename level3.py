import urllib2 
import re
import locale
import request

headers = { 'User-Agent' :  'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:25.0) Gecko/20100101 Firefox/25.0',
            'Cookie' :  'd53db4de415c4e858dc761595623a898=+; Path=/\r\n'  }
request = request.RequestUrl()
site_status_1 = request.open_url_and_get_content('http://hughes.sieve.com.br:8000/level3/', headers=headers)
pattern = r'href="(.*?)"'
match = re.search(pattern, site_status_1)
site_status_2 = request.open_url_and_get_content('http://hughes.sieve.com.br:8000' + match.groups()[0], headers=headers)
headers = { 'User-Agent' :  'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:25.0) Gecko/20100101 Firefox/25.0',
            'Cookie' :  'd53db4de415c4e858dc761595623a898=+; Path=/\r\n',
            'Cookie' :  '18=+;'
             }
site_status_3 = request.open_url_and_get_content('http://hughes.sieve.com.br:8000/level3/', headers=headers)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
pattern = r'R\$ ([\d\.,]+)'
match = re.search(pattern, site_status_3)
price = locale.atof(match.groups()[0])
print 'R$ %f' % price 
