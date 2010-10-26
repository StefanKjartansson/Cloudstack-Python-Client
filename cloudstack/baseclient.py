import urllib2
import urllib
import hashlib
import json
import time
import socket
import os
import logging
import hmac
import base64

from cloud_exceptions import CloudException
from dataobject import *


__all__ = ['BaseClient', 'DataObject', 'CloudException']


logger = logging.getLogger('cloud_com.baseclient')


class BaseClient(object):

    def __init__(self, url, username=None, password=None,
        apiKey=None, secretKey=None, password_encode=True):
        '''
        url and either a username and password or apiKey and secretKey
        '''

        self.use_login = False
        if username and password:
            self.use_login = True

        if self.use_login:
            self.username = username
            self.password = password
        elif (apiKey and secretKey):
            self.apiKey = apiKey
        else:
            raise Exception('''Either provide a valid set of
                username--password or apiKey--secretKey''')

        self.url = url
        if self.url.endswith('?'):
            self.url = self.url[:-1]

        if self.use_login:
            self.caller = urllib2.build_opener(
                urllib2.HTTPCookieProcessor())
            urllib2.install_opener(self.caller)
            #Will throw error if login fails.
            self.login_response = self.__execute__('login', {
                'username': self.username,
                'password': (hashlib.md5(self.password).hexdigest()
                    if password_encode else self.password)})
            self.is_connected = True
        else:
            class SignatureCaller(object):
                def __init__(self, secretKey):
                    self.secretKey = secretKey

                def open(self, *args, **kwargs):
                    url = args[0]

                    base_url, query_string = url.split('?')
                    msg = '&'.join(sorted([s.lower() for s in
                        query_string.split('&')]))

                    logging.debug('unsignedRequest: %s' % msg)

                    signature = base64.b64encode(
                        hmac.new(self.secretKey,
                        msg=msg, digestmod=hashlib.sha1).digest())

                    logging.debug('Signature: %s' % signature)

                    url = '%s?%s&signature=%s' % (base_url,
                        query_string, urllib.quote(signature))

                    logging.debug('Calling API: %s' % url)

                    return urllib2.urlopen(url, **kwargs)

            self.caller = SignatureCaller(secretKey)
            self.is_connected = True

    @classmethod
    def loadFromProperties(klass, properties_file):
        if properties_file.startswith('~'):
            p = os.path.expanduser('~') + properties_file[1:]
        else:
            p = properties_file
        logger.info('Using properties file: %s' % p)
        with open(p, 'r') as f:
            properties = dict([l.split('=')
            for l in f.read().split('\n')
                if not l.startswith('#') and l is not ''])

            url = properties.pop('url', None)
            if not url:
                raise Exception('Missing url from properties')
            return klass(url, **properties)

    def __execute__(self, command, kwargs, async=False):
        try:
            if not command:
                raise Exception('Missing command!')
            kwargs = kwargs or {}
            params = dict([(k, v) for (k, v)
                in kwargs.items()
                if v is not None])
            if not self.use_login:
                params.update({'apiKey': self.apiKey})

            params.update({'command': command, 'response': 'json'})

            logger.debug('Executing command %s with arguments: %s' % (
                command, str(params)))

            if async:
                logger.debug('Command is asynchronous')
                jobid = self.process(command.lower() + 'response',
                    json.loads(self.caller.open(
                    self.url + '?' + urllib.urlencode(params)).read())).jobid
                logger.debug('Async jobid: %d' % jobid)

                job = self.queryAsyncJobResult(jobid)

                logger.debug('Async Job Info: %s' % job)

                while job.jobstatus == '0':
                    time.sleep(2)
                    job = self.queryAsyncJobResult(jobid)
                    logger.debug('Async Job Info: %s' % job)
                if job.jobstatus == '1':
                    return self.__execute__('queryAsyncJobResult',
                        {'jobid': jobid})
                elif job.jobstatus == '2':
                    raise Exception('Asynchronous exception %s: %s.' % (
                        job.jobresultcode, job.jobresult))
            return json.loads(self.caller.open(
                self.url + '?' + urllib.urlencode(params)).read())
        except urllib2.HTTPError as (errno):
            raise CloudException(errno.code)

    def process_async(self, command, kwargs, _class=DataObject):
        logger.debug(
            'Processing asynchronous command %s with arguments: %s' % (
            command, str(kwargs)))
        data = self.__execute__(command, kwargs, True)
        if data['queryasyncjobresultresponse']['jobresulttype'] == u'object':
            obj = [v[0] for (k, v)
                in data['queryasyncjobresultresponse'].items()
                if not k.startswith('job')][0]
            obj['api_client'] = self

            logging.debug('Creating %s with params: %s' % (
                str(_class), str(obj)))

            return _class(**dict([(str(k), v) for (k, v)
                in obj.items()]))
        return self.process_list(selector, data, _class)

    def process(self, selector, data, _class=DataObject):
        logger.debug('Processing result with selector: %s and data: %s' % (
            selector, str(data)))
        return _class(**dict([(str(k), v) for (k, v) in
            data.get(selector).items()] +
            [('api_client', self)]))

    def process_list(self, selector, data, _class=DataObject):
        logger.debug(
            'Processing list results with selector: %s and data: %s' % (
            selector, str(data)))

        n = data
        for i in selector.split('>'):
            n = n.get(i)
            if not n:
                logger.error(
                'Expected list, got null. Selector: %s, Data: %s' % (selector,
                    str(data)))
                return []
        return [_class(**dict([(str(k), v) for (k, v)
            in d.items()] + [('api_client', self)]))
            for d in n]
