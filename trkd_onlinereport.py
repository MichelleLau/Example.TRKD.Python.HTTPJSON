'''
The TRKD API sample code is provided for informational purposes only 
and without knowledge or assumptions of the end users development environment. 
We offer this code to provide developers practical and useful guidance while developing their own code. 
However, we do not offer support and troubleshooting of issues that are related to the use of this code 
in a particular environment; it is offered solely as sample code for guidance. 
Please see the Thomson Reuters Knowledge Direct product page at http://customers.thomsonreuters.com 
for additional information regarding the TRKD API.'''

import os
import sys
import requests
import json
import getpass

# Send HTTP request for all services
def doSendRequest(url, requestMsg, headers):
    result = None
    try:
        # send request
        result = requests.post(
            url, data=json.dumps(requestMsg), headers=headers)
        # handle error
        if result.status_code is not 200:
            print('Request fail')
            print('response status %s' % (result.status_code))
            if result.status_code == 500:  # if username or password or appid is wrong
                print('Error: %s' % (result.json()))
            result.raise_for_status()
    except requests.exceptions.RequestException as e:
        print('Exception!!!')
        print(e)
        sys.exit(1)
    return result


# Perform authentication
def CreateAuthorization(username, password, appid):
    token = None
    # create authentication request URL, message and header
    authenMsg = {'CreateServiceToken_Request_1': {
        'ApplicationID': appid, 'Username': username, 'Password': password}}
    authenURL = 'https://api.trkd.thomsonreuters.com/api/TokenManagement/TokenManagement.svc/REST/Anonymous/TokenManagement_1/CreateServiceToken_1'
    headers = {'content-type': 'application/json;charset=utf-8'}
    print('############### Sending Authentication request message to TRKD ###############')
    authenResult = doSendRequest(authenURL, authenMsg, headers)
    if authenResult is not None and authenResult.status_code == 200:
        print('Authen success')
        print('response status %s' % (authenResult.status_code))
        # get Token
        token = authenResult.json()['CreateServiceToken_Response_1']['Token']

    return token

# Perform Online Report request


def RetrieveOnlineReport(token, appid):
    # construct Online Report URL and header
    onlinereportURL = 'http://api.trkd.thomsonreuters.com/api/OnlineReports/OnlineReports.svc/REST/OnlineReports_1/GetSummaryByTopic_1'
    headers = {'content-type': 'application/json;charset=utf-8',
               'X-Trkd-Auth-ApplicationID': appid, 'X-Trkd-Auth-Token': token}
    # construct a Online Report request message
    onelinereportRequestMsg = {'GetSummaryByTopic_Request_1': {
        'Topic': 'OLRUTOPNEWS',
        'MaxCount': 20,
        'ReturnPrivateNetworkURL': False
    }
    }
    print('############### Sending News - Online Report request message to TRKD ###############')
    onlinereportResult = doSendRequest(
        onlinereportURL, onelinereportRequestMsg, headers)
    if onlinereportResult is not None and onlinereportResult.status_code == 200:
        print('Online Report response message: ')
        print(onlinereportResult.json())



## ------------------------------------------ Main App ------------------------------------------ ##

if __name__ == '__main__':
    # Get username, password and applicationid
    username = input('Please input username: ')
    # use getpass.getpass to hide user inputted password
    password = getpass.getpass(prompt='Please input password: ')
    appid = input('Please input appid: ')

    token = CreateAuthorization(username, password, appid)
    print('Token = %s' % (token))

    # if authentiacation success, continue subscribing Online Report
    if token is not None:
        RetrieveOnlineReport(token, appid)
