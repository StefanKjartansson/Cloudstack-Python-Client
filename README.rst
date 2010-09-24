--------------
Cloud.com Cloudstack Client
--------------

Provides a simple python client to cloud.com's api. 

=========
Installation
=========

1. Checkout repository
2. sudo python setup.py install


=========
Usage
=========

>>> from cloudstack import Client
>>> c = Client('http://mycloud/client/api', apiKey='my_api_key', secretKey='my_secret_key')
>>> print c.listVirtualMachines()

  
============
Requirements
============
 
 - **nose** (for unit tests *optional*)

