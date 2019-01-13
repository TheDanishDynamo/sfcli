"""
Connect to salesforce REST API to authenticate.
https://sforce.co/1RDG1os
Parameter	    Description
grant_type	    Must be password for this authentication flow.
client_id	    The Consumer Key from the connected app definition.
client_secret	The Consumer Secret from the connected app definition. Required unless the Require Secret for Web Server Flow setting is not enabled in the connected app definition.
username	    End-user’s username.
password	    End-user’s password.

Note: You must append the user’s security token to their password A security token is an 
automatically-generated key from Salesforce. For example, if a user's password is mypassword, 
and their security token is XXXXXXXXXX, then the value provided for this parmeter must be 
mypasswordXXXXXXXXXX. For more information on security tokens see “Reset Your Security Token” 
in the online help.

An example request body [querystring] might look something like the following:

grant_type=password
&client_id=3MVG9lKcPoNINVBIPJjdw1J9LLM82HnFVVX19KY1uA5mu0QqEWhqKpoW3svG3XHrXDiCQjK1mdgAvhCscA9GE
&client_secret=1955279925675241571
&username=testuser%40salesforce.com
&password=mypassword123456

client_id and client_secret
If you navigate to Create --> Apps --> you can see connected apps, click on it and you 
can see consumer key (client_id) and consumer secret (client_secret). 

token
For the security token you can (login with api username), then get the token via email when you go to 
my settings --> personal --> reset my security token. 
"""

import http.client
from config import cfg # private configuration, clone config.py.template
from requests.utils import requote_uri

# Build Token Request Data
qs = ""
qs += "grant_type=password"	  
qs += "&client_id=" + cfg.sf_api_client_id	  
qs += "&client_secret=" + cfg.sf_api_client_secret
qs += "&username=" + cfg.sf_api_username
qs += "&password=" + cfg.sf_api_password  
qs += cfg.sf_api_security_token

# Set server
conn = http.client.HTTPSConnection(cfg.sf_api_auth_token_host)

# HTTP post data
print('Posting to here ' + cfg.sf_api_auth_token_host)
print('Posting this ' + requote_uri(qs))
#exit()

# Request plus header application/x-www-form-urlencoded
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn.request("POST", "/services/oauth2/token", qs, headers)
response = conn.getresponse()

# HTTP status code
print(response.status, response.reason)

# HTTP response body
vjson = response.read()

# output raw json with versions
print(vjson)

# json to panda dataframe
#vdf = pd.read_json(vjson)

# output table with versions
#print(vdf)


