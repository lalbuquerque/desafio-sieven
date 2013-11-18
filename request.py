import urllib
import urllib2

class RequestUrl:

    def open_url_and_get_content(self, url, data=None, headers={}, replaces={}):
        request = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(request)
        feeddata = response.read()
        if replaces is not None:
            for k, v in replaces.items():
                url = response.geturl().replace(k, v)
                request = urllib2.Request(url, data, headers)
                response = urllib2.urlopen(request)
                feeddata = response.read()
        return feeddata
