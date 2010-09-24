import time
import hashlib
import sys
import urllib
import urllib2
import os
from nose import with_setup

from client import Client, VMSTATE


class Tests(object):

    def setUp(self):
        "Load configuration from properties file."
        with open(os.path.expanduser('~') + '/greenqloud.properties',
                'r') as f:
            properties = dict([l.split('=') for l in f.read().split('\n')
                if not l.startswith('#')
                and l.strip() is not ''])
            self.url = properties.get('url')
            self.api = properties.get('apiKey')
            self.key = properties.get('secretKey')

    def tearDown(self):
        "tear down test fixtures"
        pass

    def test_listVirtualMachines(self):
        vms = Client(self.url,
            apiKey=self.api,
            secretKey=self.key).listVirtualMachines()
        assert vms
        assert (len(vms) > 0)
