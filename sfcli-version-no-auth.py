import http.client
from config import cfg # private configuration
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


