import unittest
import httplib
import json
import sys

class TestGreetingService(unittest.TestCase):
    """
    Test the add function from the calc library
    """

    def test_available(self):
        """
        """
        conn = conn = httplib.HTTPConnection("AJ006717", 9080)
        conn.request("GET", "/greeting")
        r1 = conn.getresponse()
        print r1.status, r1.reason
        self.assertEqual(r1.status, 200)



    def test_version(self):
        """
        """
        conn = conn = httplib.HTTPConnection("AJ006717", 9080)
        conn.request("GET", "/greeting")
        r1 = conn.getresponse()
        print r1.status, r1.reason
        self.assertEqual(r1.status, 200)
        data = json.load(r1)
        self.assertEqual(data['version'] ,'2.0')



