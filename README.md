# sfcli

An experimental rest client to salesforce (API v 44).

My environment is macos (linux/darwin) with python3 v 3.7.1. It's possible that this will run on other platforms and versions. Cross platform is out of scope, basically you need some OS with Python and a text editor, and internet access, and at some point in the project you need a salesforce instance with admin access, e.g. a free developer instance from www.salesforce.com.

### Finding the latest Salesforce REST api documentation
... google it, like so https://www.google.com/search?q=salesforce+rest+api

in January 2019 this is what came up:

https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.htm


### Files
[sfcli-version-no-auth.py](sfcli-version-no-auth.py) contains python code to get current API versions. The API version list "method" does not require authorization, so this is a minimalistic example of calling API and using the result using python libraries. This requires the name of an instance. You can also open the api directly in the browser, try this https://myinstance.salesforce.com/services/data/ .. it will not work!! Why? Because you need to replace the "myinstance" part with the part of the address you see when you log in to www.salesforce.com.

(Ignore the following step if you are not running macOS)
Before you run this on macOS you have to do this:

Open Terminal
```
cd /Applications/Python\ 3.7/
./Install\ Certificates.command 
```

[sfcli-get-auth-token.py](sfcli-get-auth-token.py) contains python code to authenticate. 




