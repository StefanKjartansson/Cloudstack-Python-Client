
__all__ = ['CloudException']


class CloudException(Exception):
    mapper = {
        '503': 'Service unavailable',
        '531': 'Account error',
        '401': 'Unauthorized user',
        '430': 'Malformed parameters',
        '530': 'Internal server error',
        '436': 'Invalid domain ID',
    }

    def __init__(self, code):
        super(CloudException, self).__init__(self.mapper.get(str(code),
            'Error code %d is undefined' % code))
