import urllib2 
import re
import locale
import request

request = request.RequestUrl()
headers = { 'User-Agent' :  'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:25.0) Gecko/20100101 Firefox/25.0',
            'Cookie'     :  'd53db4de415c4e858dc761595623a898=+; 18=+; cade-meu-cookie=\"esta aqui\";' 
            }
feeddata = request.open_url_and_get_content('http://hughes.sieve.com.br:8000/level5/', headers=headers, replaces={ '%' : '%25'})
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
string = re.sub('\s', '', feeddata)
pattern = r'R\$([\d\.,]+)'
match = re.search(pattern, string)
price = locale.atof(match.groups()[0])
print 'R$ %f' % price 
