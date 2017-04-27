# Introduction
This is an example project that shows how to implement TRKD REST Client with python
- trkd_authen.py: An example application that shows how to authenticate with TRKD service
- trkd_quote.py: An example application that shows how to subscribe (all fields and specific fields) the Quote data from TRKD service
- trkd_newsheadline.py: An example application that shows how to subscribe the News Headline data from TRKD service
- trkd_newsstory.py: An example application that shows how to subscribe the News Story data from TRKD service
- trkd_intraday.py: An example application that shows how to subscribe the Intraday Time-series data from TRKD service
- trkd_interday.py: An example application that shows how to subscribe the Interday Time-series data from TRKD service
- trkd_onlinereport.py: An example application that shows how to subscribe the Online Report data from TRKD service
- trkd_chart.py: An example application that shows how to subscribe and download the Chart image data from TRKD service
- docs\TRKD_REST_with_Python.docx: A document that describes the trkd_authen.py and trkd_quote.py applications 


# prerequisite
The following softwares are required to use this script
- Python 2.7.10
- The [requests](http://docs.python-requests.org/en/master/) library 

The script does not support Python 3!

# how to run the script
Run the script via the command line (or shell)
```
$>python <application>.py
```

# Optional - How to install requests
The best way is to get the pip package management tool 
1. export <Python_folder>\Scripts to your OS PATH environment
2. call pip command to install requests
	```
	$>pip install requests
	```
3. If you are behind proxy, set the proxy first
	```
	export https_proxy="http://<proxy.server>:<port>"
	$>pip install requests
	```
#Releae Note
- Version 1: 6 Sep 2016
    - trkd_authen.py
	- trkd_quote.py
- Version 1.0.1: 7 Sep 2016
	- trkd_newsheadline.py
	- changed code structure to separate call http request 
- Version 1.0.2: 19 Sep 2016
	- trkd_newsstory.py
- version 1.0.3: 22 Sep 2016
	- trkd_intraday.py
	- trkd_interday.py
	- trkd_onlinereport.py
	- trkd_chart.py
- version 1.0.4: 28 Oct 2016
	- docs\TRKD_REST_with_Python.docx
	- revise some code
- version 1.0.5: 27 Apr 2017
	- revies README.md to support markdown
	