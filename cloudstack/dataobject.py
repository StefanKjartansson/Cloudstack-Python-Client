import datetime
import logging
from functools import wraps

__all__ = ['DataObject', 'expect_single']


logger = logging.getLogger('cloud_com.dataobject')


def expect_single(f):
    def new_func(*args, **kwargs):
        res = f(*args, **kwargs)
        if not res:
            logger.error('Result was null')
            return None
        if len(res) == 0:
            return []
        elif len(res) > 1:
            logger.error(
                'Expected single return value when calling %s, got %d.'
                % (f.func_name, len(res)))
        return res[0]
    return new_func


class DataObject(object):

    def __init__(self, **data):
        """
        Inherit the DataObject to provide custom functionality.
        """

        def format_type(k, v):
            if v == 'null':
                return None
            return v if isinstance(v, list) else \
                datetime.datetime.strptime(v[:-6], "%Y-%m-%dT%H:%M:%S") if (
                    v.endswith('created')) else \
                int(v) if (k.endswith('id') or
                           k.endswith('code') or
                           k.endswith('port') or
                           k.endswith('number')) else \
                True if (v.strip() == 'true') else \
                False if (v.strip() == 'false') else v
        [setattr(self, k, format_type(k, v))
            for (k, v) in data.items() if k != 'api_client']
        setattr(self, 'api_client', data.get('api_client', None))

        if not hasattr(self, 'api_client'):
            logger.warn('Created DataObject with no api_client')

    @property
    def valid_api(self):
        """Shorthand to make sure the api client valid."""
        return (hasattr(self, 'api_client') and self.api_client != None and \
            ((self.api_client.use_login and self.api_client.is_connected) or \
            not self.api_client.use_login))

    def __repr__(self):
        return '%s: %s' % (super(DataObject, self).__repr__(),
            str(self.__dict__))

    def __str__(self):
        return str(self.__dict__)
