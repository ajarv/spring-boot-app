import httplib
import json
import sys

def t1():
    conn = conn = httplib.HTTPConnection("AJ006717", 9080)
    conn.request("GET", "/greeting")
    r1 = conn.getresponse()
    print r1.status, r1.reason
    print 'Test Successful'
    return 0

rcode = t1()
sys.exit(rcode)

