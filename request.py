import urllib
import urllib2

class RequestUrl:

    def open_url_and_get_content(self, url, data=None, headers={}):
        #headers = urllib.urlencode(params)
        request = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(request)
        feeddata = response.read()
        return feeddata
