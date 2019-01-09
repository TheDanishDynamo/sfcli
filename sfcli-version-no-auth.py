import http.client
from config import cfg

host = cfg.sf_instance + ".salesforce.com"
conn = http.client.HTTPSConnection(host)
print('Get API Data from ' + host + '/services/data/')
conn.request("GET", "/services/data/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()
print(data1)
