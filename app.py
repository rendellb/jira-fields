from requests import get
from json import loads
from jiraconfig import *

def dumpFields(issueKey):
    getUrl =  apiBase + '/issue/' + issueKey
    getResponse = get(getUrl, headers=headersGetJira)
    data = loads(getResponse.text)
    
    dumpParse(data, '')
    
def searchFields(issueKey, value):
    getUrl =  apiBase + '/issue/' + issueKey
    getResponse = get(getUrl, headers=headersGetJira)
    data = loads(getResponse.text)
    
    searchParse(data, '', value)
    
def dumpParse(data, fieldStr):
    if type(data) is dict:
        for key in data:
            fieldPath = fieldStr + "['" + str(key) + "']"
            if type(data[key]) is dict:
                dumpParse(data[key], fieldPath)
            elif type(data[key]) is list:
                for idx, row in enumerate(data[key]):
                    dumpParse(data[key][idx], fieldPath + "[" + str(idx) + "]")
            else:
                value = 'null'
                try:
                    value = data[key].encode('utf-8')
                except:
                    pass
                print fieldPath + ': ' + str(value)
    elif type(data) is list:
        for idx, row in enumerate(data):
            dumpParse(data[idx], fieldPath + "[" + str(idx) + "]")
            
def searchParse(data, fieldStr, value):
    if type(data) is dict:
        for key in data:
            fieldPath = fieldStr + "['" + str(key) + "']"
            if type(data[key]) is dict:
                searchParse(data[key], fieldPath, value)
            elif type(data[key]) is list:
                for idx, row in enumerate(data[key]):
                    searchParse(data[key][idx], fieldPath + "[" + str(idx) + "]", value)
            else:
                try:
                    if data[key].encode('utf-8') == value:
                        print fieldPath
                except:
                    pass
    elif type(data) is list:
        for idx, row in enumerate(data):
            searchParse(data[idx], fieldPath + "[" + str(idx) + "]", value)