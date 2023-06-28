import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse

class URLRequest(object):
    def get(self, url_request, proxy_address):
        try:
            parse = urlparse(proxy_address)
            proxy_scheme = parse.scheme
            proxy = str(parse.hostname) + ':' + str(parse.port)
            proxy_handler = urllib.request.ProxyHandler({proxy_scheme: proxy})
            opener = urllib.request.build_opener(proxy_handler)
            urllib.request.install_opener(opener)
            req = urllib.request.Request(url_request)
            data = urllib.request.urlopen(req, timeout=1)
            
            return data
        except urllib.error.HTTPError as e:
            return e.code
        except urllib.error.URLError as e:
            return e.reason
        except Exception as detail:
            pass

if __name__ == '__main__':
    url_request = URLRequest()
    # Use the URLRequest object as needed
