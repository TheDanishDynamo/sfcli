import http.client
from config import cfg
import json
import pandas as pd

host = cfg.sf_instance + ".salesforce.com"
conn = http.client.HTTPSConnection(host)
print('Get API Data from ' + host + '/services/data/')
conn.request("GET", "/services/data/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()
print(data1)

po = pd.read_json(data1)

print(po)


