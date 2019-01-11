"""
Connect to salesforce REST API to get versions e.g.
         label                   url  version
0   Winter '11  /services/data/v20.0       20
24  Winter '19  /services/data/v44.0       44
"""

import http.client
from config import cfg # private configuration, clone config.py.template
import pandas as pd

host = cfg.sf_instance + ".salesforce.com"

# Set server
conn = http.client.HTTPSConnection(host)
print('Get API Data from ' + host + '/services/data/')

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


