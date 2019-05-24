# DAPNET Python3 Call and News Framework
This is a proof of concept framework build in pyhton3 for usage on DAPNET Pocsag paging network (see https//www.hampager.de).

## Usage
To use the Classes, simply import them into your python code like:
```
#!/usr/bin/python3
# -*- coding: utf-8 -*-
from DAPNET import Call
import configuration

call = Call(configuration.dapnetuser, configuration.dapnetpasswd)

call.send("Testmessage", ["dg9vh"], ["dl-sl"])

```

You also need to create a file named configuration.py for this with following content:
```
#!/usr/bin/python3
# -*- coding: utf-8 -*-
dapnetuser = "YOURDAPNETLOGIN"
dapnetpasswd = "YOURDAPNETPASSWORD"

```
An example for this file is also in this repository.

## Functions
There are two main functional classes:
### News
For sending news, you need this lines of code:
```
news = News(configuration.dapnetuser, configuration.dapnetpasswd, "https://hampager.de/api")
```
if connecting to DAPNET via internet or
```
news = News(configuration.dapnetuser, configuration.dapnetpasswd)
```
if using hamnet-connection.

To issue a news-message, use this code-line afterwards:
```
news.send("Here stands your message text", "rubricname", 1)
```
where the number at the end is the message-number within the skyper-rubric (1 to 10)

### Call
For sending calls, you need this lines of code:
```
call = Call(configuration.dapnetuser, configuration.dapnetpasswd, "https://hampager.de/api")
```
if connecting to DAPNET via internet or
```
call = Call(configuration.dapnetuser, configuration.dapnetpasswd)
```
if using hamnet-connection.

To issue a call, use this code-line afterwards:
```
call.send("Testmessage", ["dg9vh"], ["dl-sl"])
```
## Further Questions?
If you have any questions, do not be shy and ask me via telegram (@Kim_DG9VH) or drop me an email: dg9vh@darc.de