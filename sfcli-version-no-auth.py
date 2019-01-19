"""
Connect to salesforce REST API to get versions e.g.
         label                   url  version
0   Winter '11  /services/data/v20.0       20
24  Winter '19  /services/data/v44.0       44
"""

import http.client
from config import cfg # private configuration, clone config.py.template
import pandas as pd

environment = cfg.sf_api_instance + '.' + cfg.sf_api_host

# Set server
conn = http.client.HTTPSConnection(environment)
print('Get API Data from ' + environment + '/services/data/')

# HTTP get data
conn.request("GET", "/services/data/")
response = conn.getresponse()

# HTTP status code
print(response.status, response.reason)

# HTTP response body
vjson = response.read()

# output raw json with versions
print(vjson)

# json to panda dataframe
vdf = pd.read_json(vjson)

# output table with versions
print(vdf)


