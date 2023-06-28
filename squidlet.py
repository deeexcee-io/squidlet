import sys
import socket
import ssl
import argparse
import threading
from url_request import URLRequest

class PortScanner(threading.Thread):
    def __init__(self, target, port, proxy):
        threading.Thread.__init__(self)
        self.target = target
        self.port = port
        self.proxy = proxy

    def run(self):
        req = URLRequest()
        try:
            data = req.get("http://{}:{}".format(self.target, str(self.port)), "{}".format(self.proxy))
            code = data.getcode()
            if code == 200 or code == 404 or code == 401 or code == 302:
                print("{} {} seems OPEN".format(self.target, str(self.port)))
        except:
            pass

class Spose(object):
    def __init__(self):
        parser = argparse.ArgumentParser(
            prog='Squidlet by Deeexcee, forked and borked from Spose by Petruknisme',
            description='Squid Pivoting Open Port Scanner'
        )
        parser.add_argument("--proxy", help="Define proxy address url(http://xxx:3128)",
                            action="store", dest='proxy')
        parser.add_argument("--target", help="Define target IP behind proxy",
                            action="store", dest='target')
        parser.add_argument("--threads", help="Number of threads to use for scanning",
                            action="store", dest='threads', type=int, default=10)
        results = parser.parse_args()

        if results.target is None or results.proxy is None:
            parser.print_help()
            sys.exit()

        self.target = results.target
        self.proxy = results.proxy
        self.threads = results.threads

        print("Using proxy address {}".format(self.proxy))

    def scan_ports(self):
        threads = []
        for port in range(1, 65536):
            thread = PortScanner(self.target, port, self.proxy)
            thread.start()
            threads.append(thread)

            # Limit the number of active threads
            if len(threads) >= self.threads:
                for t in threads:
                    t.join()
                threads = []

        # Wait for the remaining threads to complete
        for thread in threads:
            thread.join()

if __name__ == '__main__':
    spose = Spose()
    spose.scan_ports()
