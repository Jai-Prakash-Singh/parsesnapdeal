import urllib2
from random import choice

def main(link):
    f = open("/home/user/Desktop/prox300114")
    iplist = f.read().strip().split("\n")
    ip = choice(iplist).strip()
    f.close()

    proxy = urllib2.ProxyHandler({'http': 'http://vinku:india123@'+ip})
    auth = urllib2.HTTPBasicAuthHandler()
    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    conn = urllib2.urlopen(link)
    return   conn
